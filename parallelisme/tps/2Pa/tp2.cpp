#include <mpi.h>
#include <iostream>
#include <vector>
#include <list>
#include "Array2D.hpp"
#include "Point.hpp"

std::vector<Point> listToVector(std::list<Point> l){
	std::vector<Point> v(l.size());
	int i= 0;
	for(Point p : l){
		v.at(i)= p;
		i++;
	}
	return v;
}

std::list<Point> getDiagonale(int n, Array2D<int> a){
	std::list<Point> l;
	Point p(n, 0);
	Point t(-1, 1);
 	for(int i= 0; i <= n; i++){
		if(a.isIn(p)){
			l.push_back(p);
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
	
	int width= 3;
	int height= 3;
	
	if(myRank == nProc-1){
		Array2D<int> a(3,3,0);
		std::list<Point> l= getDiagonale(2, a);
		std::vector<Point> v= listToVector(l);
		for(int i= 0; i < nProc-1; i++){
			MPI_Send(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD);
		}
		std::cout << "Je suis le processeur " << myRank << " et j'ai tout envoyé" << std::endl;
	}
	else{
		std::vector<Point> v(std::max(width, height));
		MPI_Status status;
		MPI_Recv(v.data(), v.size(), MPI_INT, nProc-1, 0, MPI_COMM_WORLD, &status);
		std::cout << "Je suis le processus: " << myRank << " et j'ai reçu le vecteur"<< std::endl;
	}
	MPI_Finalize();
}

