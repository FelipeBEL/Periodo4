#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(){
    int i;
    float random, media=0,c,d;
    int *face;

    face = (int *) malloc(1000 * sizeof(int));
    
    srand(time(NULL));

    for(i=0;i<1000;i++){
        random = (float)rand()/(float)(RAND_MAX);
        
        if(random < 1.0/6.0) face[i] = 1;
        if((random >= 1.0/6.0) && (random < 2.0/6.0)) face[i] = 2;
        if((random >= 2.0/6.0) && (random < 3.0/6.0)) face[i] = 3;
        if((random >= 3.0/6.0) && (random < 4.0/6.0)) face[i] = 4;
        if((random >= 4.0/6.0) && (random < 5.0/6.0)) face[i] = 5;
        if(random >= 5.0/6.0) face[i] = 6;
        
    }

    for(i=0;i<1000;i++){
        media += face[i];
    }

    media /= 1000;

    printf("M = %.3f\n",media);

    free(face);

    return 0;
}