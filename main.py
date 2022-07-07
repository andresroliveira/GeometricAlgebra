import numpy as np
from CliffordVector import CliffordVector
from EuclideanVector import EuclideanVector

if __name__ == '__main__':
    v = EuclideanVector(v = [1, 0, -1])

    print(v)
    print(int(v))
    print(list(v))

    v = v.transform([[1, 1, 0], [0, 0, 1]])

    print(v)
    print(int(v))
    print(list(v))
