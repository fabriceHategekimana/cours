#include <mpi.h>
#include <iostream>
#include <cmath>
#include <vector>
#include <list>
#include <iterator>
#include <fstream>
#include "Array2D.hpp"
#include "Point.hpp"

// Sauvegarde d'une matrice dans un fichier texte
void save(Array2D<double> &matrix, std::string name) {
  std::ofstream file(name.c_str());
  for (int iY=0; iY<matrix.sizeY(); ++iY) {
     copy(&matrix.data()[iY*matrix.sizeX()], &matrix.data()[iY*matrix.sizeX()]+matrix.sizeX(),
          std::ostream_iterator<double>(file, " "));
     file << "\n";
  }
}
//Calcule le nombre de point/cellule que va prendre chaque processus
int pointsParProcessus(int nbRank, int nbProc, int nbPoints){
	int np= (int) nbProc;
	int p= (int) nbPoints;
	int nr= (int) nbRank;

	int valeur= p/np;
	int reste= p%np;

	if(reste > 0 && nr+1 <= reste){
		valeur++;	
	}
	return valeur;
}

Array2D<double> TemperatureAuxBords(Array2D<double> a, double temperature){
	for(int i= 0; i < a.sizeX()-1; i++){
		a(i, 0)= temperature;
	}
	for(int i= 1; i < a.sizeY(); i++){
		a(0, i)= temperature;
	}
	return a;
}

std::vector<double> getVoisins(Point p, Array2D<double> a){
	std::vector<double> v(4,0);
	//le vecteur sera [Gauche, Droite, Haut, Bas]
	Point Gauche= p.plus(1,0);
	Point Droite= p.plus(-1,0);
	Point Haut= p.plus(0,1);
	Point Bas= p.plus(0,-1);
	if(a.isIn(Gauche)){
		v.at(0)= a(Gauche);
	}
	if(a.isIn(Droite)){
		v.at(1)= a(Droite);
	}
	if(a.isIn(Haut)){
		v.at(2)= a(Haut);
	}
	if(a.isIn(Bas)){
		v.at(3)= a(Bas);
	}
	return v;

}

double calcule(std::vector<double> v){
	//On fait la somme
	double sum= 0;
	for(auto i: v){
		sum += i;
	}
	//On divise par 4	
	return sum/4;
}

std::vector<Point> listToVector(std::list<Point> l){
	std::vector<Point> v(l.size());
	int i= 0;
	for(Point p : l){
		v.at(i)= p;
		i++;
	}
	return v;
}

std::list<Point> getDiagonale(int n, Array2D<double> a){
	std::list<Point> l;
	Point p(n, 0);
	Point t(-1, 1);
 	for(int i= 0; i <= n; i++){
		if(a.isIn(p)){
			if(a(p) != a.max()){
				l.push_back(p);
			}
		}
		p= p.plus(t);
	}	
	return l;
}

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);

	std::cout << "" << std::endl;
	
	//Définition du tableau	
	double width= std::stoi(argv[1]);
	double height= std::stoi(argv[2]);
	int iteration= std::stoi(argv[3]);

	int maxDiagonale= width+height-1;
	Array2D<double> tab(width, height, 0);

	//Mise de la température aux bords(bas et droite)
	tab= TemperatureAuxBords(tab, 4);
	if(myRank == nProc-1){
		tab.show();
	}
	std::cout << "" << std::endl;
	for(int a= 0; a < iteration; a++){
		for(int b= 2; b < maxDiagonale; b++){
			//données de la tables (doivent rester global)
			auto vtab= tab.getVector();
			auto ctab= tab.getColumn();

			MPI_Barrier(MPI_COMM_WORLD);

			if(myRank == nProc-1){
				for(int i= 0; i < nProc-1; i++){
					MPI_Send(vtab.data(), vtab.size(), MPI_INT, i, 0, MPI_COMM_WORLD);
				}
			}
			else{
				MPI_Status status;
				MPI_Recv(vtab.data(), vtab.size(), MPI_INT, nProc-1, 0, MPI_COMM_WORLD, &status);
				tab.setVector(vtab);
			}
			//Chacun trouve les points de la diagonales
			std::list<Point> l= getDiagonale(b, tab);
			auto diagonale= listToVector(l);
			std::vector<double> reponsePartielle;
			for(int i= myRank; i<diagonale.size(); i= i+nProc){ 
				//on trouve les valeurs voisines du point
				std::vector<double> voisins= getVoisins(diagonale.at(i), tab);
				//on calcule avec la Formule de Laplace
				double cv= calcule(voisins);
				reponsePartielle.push_back(cv);
				//std::cout << "p" << myRank << " => ind:" << i << " res: " << cv << std::endl;
			}
			//on se met d'accord sur la taille des données à envoyer
			if(myRank == nProc-1){
				//le dernier processus à la tâche de rassembler toutes les réponses "partielles"
				std::vector<double> reponse(diagonale.size());
				MPI_Status status;
				for(int i= 0; i < nProc-1; i++){
					int ppp= pointsParProcessus(i, nProc, diagonale.size());
					std::vector<double> part(ppp);
					MPI_Recv(part.data(), part.size(), MPI_INT, i, 0, MPI_COMM_WORLD, &status);
					for(int j= 0; j < part.size(); j++){
						reponse.at(i+(j*nProc))= part.at(j);
					}
				}
				for(int i= 0; i < reponsePartielle.size(); i++){
					reponse.at(myRank+(i*nProc))= reponsePartielle.at(i);
				}
				for(int i= 0; i < reponse.size(); i++){
					tab(diagonale.at(i))= reponse.at(i);
				}
			}
			else{
				int ppp= pointsParProcessus(myRank, nProc, diagonale.size());
				MPI_Send(reponsePartielle.data(), ppp, MPI_INT, nProc-1, 0, MPI_COMM_WORLD);
			}
			MPI_Barrier(MPI_COMM_WORLD);
		}
	}
	if(myRank == nProc-1){
		tab.show();
		save(tab, "chaleur.dat");
	}
	MPI_Finalize();
}

