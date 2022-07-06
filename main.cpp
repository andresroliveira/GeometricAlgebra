#include <bits/stdc++.h>
#include "EuclideanVector.h"

using namespace std;

int main(){
    EuclideanVector v = EuclideanVector();
    // v.print();
    int U[] = {1, 2, 3};
    EuclideanVector u = EuclideanVector(U);
    u.print();
    EuclideanVector w = v.sum(u);
    w.print();
    v.print();
    return 0;
}