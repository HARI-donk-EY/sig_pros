#include <stdio.h>
#include <math.h>
#include<stdlib.h>
#include "../header.h"

#define pi 3.14159
  
int main(){

int N=20;

double *xk = readData("../6.1/xkreal.dat",N);
double *hk = readData("../6.1/hkreal.dat",N);

double *Yk=(double*)malloc(N*sizeof(double));

for(int k=0;k<N;k++){
Yk[k] = xk[k]*hk[k];
printf("%lf \n",Yk[k]);
}

printf("\n");

createDat("ykreal.dat",N,Yk);

free(Yk);
free(xk);
free(hk);


}


