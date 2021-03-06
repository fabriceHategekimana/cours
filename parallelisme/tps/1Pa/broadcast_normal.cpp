
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

	std::vector<int> vector(100000000, 0);
	if(myRank == 0) vector = std::vector<int>(100000000, 1);
	
 	MPI_Bcast( vector.data(), vector.size(), MPI_INT, 0, MPI_COMM_WORLD );

 	std::cout << "myRank : " << myRank << ", value in the vector : " << vector.at(0) << std::endl;

	MPI_Barrier(MPI_COMM_WORLD);
	double end = MPI_Wtime();

	if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;
	MPI_Finalize();
}

