#include  <stdio.h>


void pong();

void ping(){
int j=0;
while(1){
   printf("ping %d",j++);
   pong();
}
}

void pong(){
int j=0;
while(1){
   printf("                  pong %d\n",j++);
   ping();
}
}

void main(){

ping();

} 
