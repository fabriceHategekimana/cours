
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);

	MPI_Finalize();
}

