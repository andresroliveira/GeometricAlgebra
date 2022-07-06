#include "CliffordVector.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdexcept>

CliffordVector::CliffordVector(){
    this->n = 3;
    this->v = (float*) calloc(1<<n, sizeof(float));
}

CliffordVector::CliffordVector(int dim){
    this->n = dim;
    this->v = (float*) calloc(1<<n, sizeof(float));
}

CliffordVector::~CliffordVector(){
    free(v);
}