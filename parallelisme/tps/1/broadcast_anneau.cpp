#include <mpi.h>
#include <iostream>
#include <vector>

//tableau de 100'000'000 de int avec 1, 2, 4, 8, 16, 32 et 64 coeurs
int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);

	MPI_Barrier(MPI_COMM_WORLD);
	double start = MPI_Wtime();

	if(myRank == 0){
		std::vector<int> v(100000000, 1);
		for(int i= 1; i < nProc; i++){
			MPI_Send(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD);
		}
		std::cout << "processus " << myRank << " et j'ai tout envoyé" << std::endl;
	}
	else{
		std::vector<int> v(100000000, 0);
		MPI_Status status;
		MPI_Recv(v.data(), v.size(), MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
		std::cout << "Je suis le processus " << myRank << " et j'ai reçu ce qu'il me faut" << std::endl;
	}
	MPI_Barrier(MPI_COMM_WORLD);
	double end = MPI_Wtime();

	if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;

	MPI_Finalize();
}

