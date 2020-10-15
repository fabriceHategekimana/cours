#include <mpi.h>
#include <iostream>
#include <vector>

int main(int argc, char **argv){ 
	int myRank, nProc;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &myRank);
	MPI_Comm_size(MPI_COMM_WORLD, &nProc);
	if(myRank == 0){
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
		std::vector<int> v(10, myRank);
		int sum= 0;
		for(auto i: v)
			sum += i;
		std::cout << "Je suis le processus " << myRank << " et ma somme vaut " << sum << std::endl;
		MPI_Send(&sum, sizeof(int), MPI_INT, 0, 0, MPI_COMM_WORLD);
	}
	MPI_Finalize();
}

