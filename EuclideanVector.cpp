#include "EuclideanVector.h"
#include <stdio.h>
#include <stdlib.h>

EuclideanVector::EuclideanVector(){
    this->n = 3;
    this->v = (float*) calloc(n, sizeof(float));
}

EuclideanVector::EuclideanVector(float *u){
    this->n = (int)sizeof(u)/sizeof(u[0]);

    for(int i=0;i<this->n;i++){
        this->v[i] = u[i];
    }
}

EuclideanVector::EuclideanVector(int *u){
    this->n = (int)sizeof(u)/sizeof(u[0]);

    for(int i=0;i<this->n;i++){
        this->v[i] = (float)u[i];
    }
}

EuclideanVector::~EuclideanVector(){
    free(v);
}

int EuclideanVector::length(){
    return n;
}

void EuclideanVector::print(){
    printf("[%.2lf", v[0]);
    for(int i=1;i<n;i++){
        printf(", %.2lf", v[i]);
    }
    printf("]\n");
}