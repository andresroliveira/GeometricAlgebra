import numpy


class EuclideanVector():
    __EPS = 1E-9
    def __init__(self, n = None, v = None):
        if n == None and v == None:
            self.n = 3
            self.v = [0 for _ in range(self.n)]
        elif n != None and v == None:
            self.n = n
            self.v = [0 for _ in range(self.n)]
        elif n == None and v != None:
            self.n = len(v)
            self.v = [0 for _ in range(self.n)]
            for i in range(len(v)):
                self.v[i] = v[i]
        else:
            if n < len(v):
                raise Exception("Not compatible")
            self.n = n
            self.v = [0 for _ in range(self.n)]
            for i in range(len(v)):
                self.v[i] = v[i]

    def __getitem__(self, id):
        return self.v[id]
    
    def __setitem__(self, id, value):
        self.v[id] = value

    def __int__(self):
        return self.n

    def __list__(self):
        return self.v

    def __iter__(self):
        return iter(self.v)

    def __str__(self):
        return f'n: {self.n}, v: {self.v}'

    def __len__(self):
        return self.n

    def dim(self):
        return self.n

    def __add__(self, other):
        if self.n != other.n:
            raise Exception("Not same dim")

        new_n = self.n
        new_v = [self.v[i] for i in range(new_n)]

        for i in range(new_n):
            new_v[i] += other.v[i]

        return EuclideanVector(new_n, new_v)

    def __sub__(self, other):
        if self.n != other.n:
            raise Exception("Not same dim")

        new_n = self.n
        new_v = [self.v[i] for i in range(new_n)]

        for i in range(new_n):
            new_v[i] -= other.v[i]

        return self.__class__(new_n, new_v)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_n = self.n
            new_v = [other*self.v[i] for i in range(self.n)]
            return self.__class__(n=new_n, v=new_v)

        if self.n != other.n:
            raise Exception("Not same dim")

        return sum([ self.v[i]*other.v[i] for i in range(self.n)  ])

    def __neg__(self):
        return (-1)*self
    
    def __pos__(self):
        return self

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_n = self.n
            new_v = [self.v[i]/other for i in range(self.n)]
            return self.__class__(n=new_n, v=new_v)
        
        raise Exception("Not divide")

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_n = self.n
            new_v = [self.v[i]//other for i in range(self.n)]
            return self.__class__(n=new_n, v=new_v)
        
        raise Exception("Not divide")

    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        self = self + other
        return self

    def __imul__(self, other):
        self = self * other
        return self

    def __idiv__(self, other):
        self = self / other
        return self

    def __ifloordiv__(self, other):
        self = self // other
        return self

    def __eq__(self, other):
        if isinstance(other, EuclideanVector):
            # if isinstance(v, list)
            return self.n == other.n and self.v == other.v
        return False

    def __ne__(self, other):
        return not(self == other)

    def __abs__(self):
        return (self*self)**0.5

    def is_null(self) -> bool:
        return abs(self) < self.EPS

    def is_unitary(self) -> bool:
        return abs(abs(self) - 1) < self.EPS

    def norm(self) -> float:
        return abs(self)

    def normalize(self):
        if self.is_null():
            raise Exception("Can't normalize null vector")
        self = self / self.norm()
        return self

    def transform(self, A):
        if isinstance(A, list) or isinstance(A, numpy.ndarray):
            return self.__class__(v = list(numpy.array(A)@self.v))

        if isinstance(A, int) or isinstance(A, float):
            self *= A
            return self

        raise Exception("Can't transform")
        
    