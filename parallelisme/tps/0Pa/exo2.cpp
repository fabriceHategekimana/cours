
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);
	if(myRank == 0){
		//Distribution des vecteurs aux autres processus
		std::vector<int> v;
		for(int i= 0; i < nProc*10; i++){
			v.push_back(i);
		}
		int compteur= 1;
		std::vector<int> vs;
		for(int i= 0; i < nProc*10; i++){
			if(compteur != (i/10)+1){
				MPI_Send(vs.data(), vs.size(), MPI_INT, compteur, 0, MPI_COMM_WORLD);
				vs.clear();
				compteur++;
			}	
			vs.push_back(v[i]);
		}
		//Réception des sommes des autres processus
		MPI_Status status;
		int sum;
		int total= 0;
		for(int i= 1; i < nProc; i++){
			MPI_Recv(&sum, sizeof(int), MPI_INT, i, 0, MPI_COMM_WORLD, &status);
			total += sum;
		}
		std::cout << "processus " << myRank << " le total est: " << total << std::endl;
	}
	else{
		//réception du vecteur provenant du processus 0
		MPI_Status status;
		std::vector<int> vt(10, 0);
		MPI_Recv(vt.data(), vt.size(), MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
		int sum= 0;
		for(auto i: vt)
			sum += i;
		std::cout << "Je suis le processus " << myRank << " et ma somme vaut " << sum << std::endl;
		MPI_Send(&sum, sizeof(int), MPI_INT, 0, 0, MPI_COMM_WORLD);
	}
	MPI_Finalize();
}

