#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);
	if(myRank == 0){
		std::vector<int> v(100, 1);
		for(int i= 1; i < nProc; i++){
			MPI_Send(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD);
		}
		std::cout << "processus " << myRank << " le total est: " << total << std::endl;
	}
	else{
		MPI_Status status;
		MPI_Recv(v.data(), v.size(), MPI_INT, i, 0, MPI_COMM_WORLD, &status);
		std::vector<int> v(10, myRank);
		std::cout << "Je suis le processus " << myRank << " et ma somme vaut " << sum << std::endl;
	}
	MPI_Finalize();
}

