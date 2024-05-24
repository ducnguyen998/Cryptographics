import random

from Helper import (
    PrimeHelper
)

class EllipticCurve:
    def __init__(self, _p, _a=None, _b=None):
        self.helper = PrimeHelper()
        if _a == None and _b == None:
            _a, _b = self.__create_ellipse_coefs(_p)
        self.a = _a
        self.b = _b
        self.p = _p

    def __create_ellipse_coefs(self, p):
        a = 0
        b = 0
        while (self.__mod_faster(4 * (a ** 3) + 27 * (b ** 2), p) == 0):
            a = random.randint(-p, p)
            b = random.randint(-p, p)
        return (a, b)
    
    def __mod(self, n, p):
        return n % p
    
    def __mod_faster(self, n, p):
        return self.helper.modular_exponentiation(n, 1, p)
    
    def __compute_xy_square(self):
        self.x_square = [(self.__mod(x ** 2, self.p)) for x in range(self.p)]
        self.y_square = [(self.__mod(x ** 3 + self.a * x + self.b, self.p)) for x in range(self.p)]

    def find_ellipse(self):
        self.__compute_xy_square()
        self.ellipse = [[idx for idx, x2 in enumerate(self.x_square) if y2 == x2] for y2 in self.y_square]
        self._counts = 0
        for _pair in self.ellipse:
            self._counts += _pair.__len__()
        self._counts += 1
        self.show()

    def show(self):
        print(f'Elliptic curve (E) : y^2 = x^3 + {self.a}x + {self.b} mod {self.p}')
        print(f'-------------')
        print(f'Ellipse : {self.ellipse}')
        print(f'-------------')
        print(f'Total points : {self._counts}')
        print()
        print()

def main():

    helper = PrimeHelper()

    p = helper.create(bits_min=8, bits_max=10)

    elliptic_curve = EllipticCurve(p)
    elliptic_curve.find_ellipse()

if __name__ == '__main__':
    main()