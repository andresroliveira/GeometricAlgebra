#ifndef CLIFFORDVECTOR_H
#define CLIFFORDVECTOR_H

#pragma once

class CliffordVector
{
public:
    CliffordVector();
    CliffordVector(int);
    ~CliffordVector();

private:
    int n;
    float *v;
    const float EPS = 1e-9;
};

#endif