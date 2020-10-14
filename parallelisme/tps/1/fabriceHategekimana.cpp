#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);
	
	MPI_Barrier(MPI_COMM_WORLD);
	double start = MPI_Wtime();

	if(myRank == 0){
		std::cout << "Teste d'utilisation de baobab" << std::endl;
	}
	else{
		std::cout << "Teste d'utilisation de baobab" << std::endl;
	}
	MPI_Barrier(MPI_COMM_WORLD);
	double end = MPI_Wtime();

	if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;
	MPI_Finalize();
}

