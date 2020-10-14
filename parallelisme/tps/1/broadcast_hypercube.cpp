#include <mpi.h>
#include <iostream>
#include <vector>
#include <math.h>

int getI(int rank){
	rank++;
	int i=0;
	while(pow(2,i) < rank){ 
		i++;	
	}
	return i;
}

int getPrev(int rank){
	int i=0;
	while(pow(2,i) <= rank){ 
		i++;	
	}
	i--;
	int prev= rank-pow(2,i);
	std::cout << prev  << std::endl;
	return prev;
}

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
		int i= 0;
		int next= pow(2, i)+0; //=1
		while(next <= nProc-1){
			MPI_Send(v.data(), v.size(), MPI_INT, next, 0, MPI_COMM_WORLD);
			i++;
			next= pow(2,i)+0;
		}
		std::cout << "processus " << myRank << " et j'ai tout envoyé" << std::endl;
	}
	else { 
		//le processus reçoit
		std::vector<int> v(100000000, 0);
		MPI_Status status;
		int prev= getPrev(myRank);
			MPI_Recv(v.data(), v.size(), MPI_INT, prev, 0, MPI_COMM_WORLD, &status);
		std::cout << "Je suis le processus " << myRank << " et j'ai reçu ce qu'il me faut du processus " << prev << std::endl;
		int i= getI(myRank);
		int next= pow(2,i)+myRank;
		//std::cout << "Je suis le processus " << myRank << " et mon prochain est " << next << std::endl;
		while(next <= nProc-1){
			MPI_Send(v.data(), v.size(), MPI_INT, next, 0, MPI_COMM_WORLD);
			i++;
			next= pow(2,i)+myRank;
		}
		std::cout << "processus " << myRank << " et j'ai tout envoyé" << std::endl;
	}

	MPI_Barrier(MPI_COMM_WORLD);
	double end = MPI_Wtime();
	if(myRank==0) std::cout << "temps de l'operation : " << end-start << "[s]" << std::endl;

	MPI_Finalize();
}

