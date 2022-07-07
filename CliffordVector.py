import numpy

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


    def __eq__(self, other):
        if isinstance(other, CliffordVector):
            return self.n == other.n and self.v == other.v
        return False

    def __ne__(self, other):
        return not(self == other)

    




if __name__ == '__main__':
    V = CliffordVector(v = [1, 0, 0])
    # print(V)
    U = CliffordVector(v = [0, 1, 0])
    # print(U)

    print((4.5 + U + 4.5) - 9)






