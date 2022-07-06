#include "EuclideanVector.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdexcept>

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

EuclideanVector::EuclideanVector(int dim){
    this->n = dim;
    this->v = (float*) calloc(n, sizeof(float));
}

EuclideanVector::~EuclideanVector(){
    free(v);
}

int EuclideanVector::length(){
    return n;
}

int EuclideanVector::dim(){
    return n;
}

void EuclideanVector::print(){
    printf("[%.2lf", v[0]);
    for(int i=1;i<n;i++){
        printf(", %.2lf", v[i]);
    }
    printf("]\n");
}

bool EuclideanVector::isNull(){
    for(int i=0;i<n;i++){
        if(abs(v[i]) >= EPS) return false;
    }
    return true;
}

float EuclideanVector::norm(){
    float s = 0.0;

    for(int i=0;i<n;i++){
        s += v[i]*v[i];
    }

    return sqrt(s);
}

void EuclideanVector::normalize(){
    if(isNull()){
        throw std::invalid_argument("Null vector.");
    }

    float nr = norm();

    for(int i=0;i<this->n;i++){
        setValueIndex(i, nr*getValueIndex(i));
    }
}

float EuclideanVector::getValueIndex(int id){
    return v[id];
}

void EuclideanVector::setValueIndex(int id, float value){
    this->v[id] = value;
}

EuclideanVector EuclideanVector::sum(EuclideanVector obj){
    if(length() != obj.length()){
        throw std::invalid_argument("Not same dim.");
    }

    EuclideanVector out = EuclideanVector(obj.length());

    for(int i=0;i<this->n;i++){
        out.setValueIndex(i, getValueIndex(i) + obj.getValueIndex(i));
    }

    return out;
}

EuclideanVector EuclideanVector::multiply(float scalar){
    EuclideanVector out = EuclideanVector(length());

    for(int i=0;i<this->n;i++){
        out.setValueIndex(i, scalar*getValueIndex(i));
    }

    return out;
}