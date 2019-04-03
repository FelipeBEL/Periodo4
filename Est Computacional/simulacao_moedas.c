#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(){
    int i;
    float random, media=0;
    int *moedas;

    srand(time(NULL));

    moedas = (int *) malloc(1000 * sizeof(int));

    for(i=0;i<1000;i++){
        random = (float)rand()/(float)(RAND_MAX);

        if(random < 0.5) moedas[i] = 0;
        else moedas[i] = 1;
        
    }

    for(i=0;i<1000;i++){
        media += moedas[i];
    }

    media /= 1000;

    printf("M = %.3f\n",media);

    free(moedas);

    return 0;
}