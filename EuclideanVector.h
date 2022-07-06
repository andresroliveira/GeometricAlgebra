#ifndef EUCLIDEANVECTOR_H
#define EUCLIDEANVECTOR_H

#pragma once

class EuclideanVector{
public:
    EuclideanVector();
    EuclideanVector(float*);
    EuclideanVector(int*);
    EuclideanVector(int);
    ~EuclideanVector();
    int length();
    int dim();
    void print();
    bool isNull();
    float norm();
    void normalize();

    // Get & Set
    float getValueIndex(int);
    void setValueIndex(int, float);

    // operators
    EuclideanVector sum(EuclideanVector);
    EuclideanVector multiply(float);
private:
    int n;
    float *v;
    const float EPS = 1e-9;
};

#endif