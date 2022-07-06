#ifndef EUCLIDEANVECTOR_H
#define EUCLIDEANVECTOR_H

#pragma once

class EuclideanVector{
public:
    EuclideanVector();
    EuclideanVector(float*);
    EuclideanVector(int*);
    ~EuclideanVector();
    int length();
    void print();
private:
    int n;
    float *v;
};

#endif