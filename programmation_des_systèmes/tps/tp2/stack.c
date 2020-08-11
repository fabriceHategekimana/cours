

#include<stdlib.h>
#include<stdio.h>

struct pile{ 
	char stack[128];
	int sp;
};

//FA
void pushFA(struct pile *P, char *element){ 
	P->sp++;
	P->stack[P->sp]= element;
}
void popFA(struct pile *P){ 
	P->stack[P->sp]= 0;
	P->sp--;
}

//FD
void pushFD(struct pile *P, char *element){ 
	P->sp--;
	P->stack[P->sp]= element;
}
void popFD(struct pile *P){ 
	P->stack[P->sp]= 0;
	P->sp++;
}

//EA
void pushEA(struct pile *P, char *element){ 
	P->stack[P->sp]= element;
	P->sp++;
}
void popEA(struct pile *P){ 
	P->sp--;
	P->stack[P->sp]= 0;
}

//ED
void pushED(struct pile *P, char *element){ 
	P->stack[P->sp]= element;
	P->sp--;
}
void popED(struct pile *P){ 
	P->stack[P->sp]= 0;
	P->sp++;
}


int main(int argc, char *argv[]){
	struct pile p;
	printf("%d", p.stack[127] );
	return 0;
}


