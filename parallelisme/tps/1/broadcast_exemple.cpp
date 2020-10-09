
#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);

	std::vector<int> vector(100, 0);
	if(myRank == 0) vector = std::vector<int>(100, 1);
	
 	MPI_Bcast( vector.data(), vector.size(), MPI_INT, 0, MPI_COMM_WORLD );

 	std::cout << "myRank : " << myRank << ", value in the vector : " << vector.at(0) << std::endl;

	MPI_Finalize();
}

