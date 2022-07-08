import numpy
from __aux__methods import geometric_product, colision

class CliffordVector():
    def __init__(self, n = None, v = None):
        if n == None and v == None:
            self.n = 3
            self.v = [0 for _ in range(2 ** self.n)]
        elif n != None and v == None:
            self.n = n
            self.v = [0 for _ in range(2 ** self.n)]
        elif n == None and v != None:
            self.n = len(v)
            self.v = [0 for _ in range(2 ** self.n)]
            for i in range(len(v)):
                self.v[i+1] = v[i]
        else:
            self.n = n
            self.v = [v[i] for i in range(2 ** self.n)]
            # for i in range(len(v)):
            #     self.v[i+1] = v[i]

    def __int__(self):
        return self.n

    def __iter__(self):
        return iter(self.v)

    def __list__(self):
        return self.v

    def __str__(self):
        return f'n: {self.n}, v: {self.v}'

    def __len__(self):
        return self.n

    def dim(self):
        return self.n

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_n = self.n
            new_v = [self.v[i] for i in range(2**new_n)]
            new_v[0] += other
            return self.__class__(new_n, new_v)

        if self.n != other.n:
            raise Exception("Not same dim")

        new_n = self.n
        new_v = [self.v[i] for i in range(2**new_n)]

        for i in range(2**new_n):
            new_v[i] += other.v[i]

        return self.__class__(new_n, new_v)

    def __radd__(self, other):
        return self + other 

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_n = self.n
            new_v = [self.v[i] for i in range(2**new_n)]
            new_v[0] -= other
            return self.__class__(new_n, new_v)

        if self.n != other.n:
            raise Exception("Not same dim")

        new_n = self.n
        new_v = [self.v[i] for i in range(2**new_n)]

        for i in range(new_n):
            new_v[i] -= other.v[i]

        return self.__class__(new_n, new_v)

    def __isub__(self, other):
        self = self - other
        return self

    # Multiply

    # Inner Product
    def __or__(self, other):
        return 1/2 * (self*other + other*self)

    def __ror__(self, other):
        return self | other

    # Outer Product        

    def __xor__(self, other):
        return self*other - other*self

    def __rxor__(self, other):
        return self ^ other

    #Geometric Product
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_n = self.n
            new_v = [0 for i in range(2**new_n)]
            new_v[0] += other
            other = self.__class__(new_n, new_v)

        if self.n != other.n:
            raise Exception("Not same dim")

        out = self.__class__(self.n)

        for i in range(1 << self.n):
            for j in range(1<<other.n):
                coef, mask = geometric_product(self.v[i], i, other.v[j], j)
                out.v[mask] += coef

        return out
        # inner = self|other
        # outer = self^other

        # return inner + outer

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if isinstance(other, CliffordVector):
            return self.n == other.n and self.v == other.v
        return False

    def __ne__(self, other):
        return not(self == other)

    def __invert__(self):
        new_n = self.n
        new_v = self.v.copy()

        for i in range(len(new_v)):
            sgn = 1
            if colision(i)%4 > 1:
                sgn = -1
            new_v[i] *= sgn

        return self.__class__(new_n, new_v)



if __name__ == '__main__':
    V = CliffordVector(v = [1, 0, 0])
    print("V: ", V)
    U = CliffordVector(v = [0, 1, 0])
    print("U: ", U)

    print("U | V: ", U | V)
    print("U ^ V: ", U ^ V)
    print("V ^ U: ", V ^ U)
    print("U * V: ", U * V)
    print("V * U: ", V * U)

    print()

    print("U * U: ", U * U)
    print("U | U: ", U | U)
    print("U ^ U: ", U ^ U)

    # print("U U: ", U*U)e








