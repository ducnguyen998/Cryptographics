import random as rd

from Helper import (
    PrimeHelper
)

from Base import (
    SharableKeyCryptographic
)

class ECCryptoProvider:
    def __init__(self):
        self.helper = PrimeHelper()

    def generate_cryptographic(self, bm=7, bM=8):
        p = self.helper.create(bits_min=bm, bits_max=bM, k=64)
        a, b = 0, 0

        while (4 * (a ** 3) + 3 * (b ** 2)) % p == 0:
            a = rd.randint(1, p)
            b = rd.randint(1, p)

        return ECCrypto(curve=EllipticCurve(p, a, b))

class ECCrypto:
    def __init__(self, curve):
        self.ec = curve

class ECCryptoSignature:
    pass

class EllipticCurve:
    def __init__(self, p, a=1, b=1):
        self.p = p
        self.a = a
        self.b = b
        #
        self.q = self._find_Q_p(p)
        self.E = self._get_point_collection()
        #
        print('E = ', self.E)
        print('Total points = ', len(self.E))
    def get_y_square(self, x):
        return (x ** 3 + self.a * x + self.b) % self.p
    def get_x_square(self, x):
        return (x ** 2) % self.p
    #
    #
    #
    def _find_Q_p(self, p):
        nQ = p // 2
        Qp = [i ** 2 % p for i in range(1, nQ + 1)]
        return Qp
    def _is_y_square_in_Qp(self, x):
        return self.get_y_square(x) in self.q
    def _get_y(self, x):
        if (self._is_y_square_in_Qp(x)):
            # all y1, y2 t/m y1^2 = y2^2 = y_square is in Z_p
            # so i calculate it by get_x_square(i)
            # expected : yy = [y1, y2]
            yy = []
            y_square = self.get_y_square(x)
            for i in range(0, self.p):
                if (self.get_x_square(i) == y_square):
                    yy.append(i)
            return yy
        else:
            return None
    def _get_point_collection(self):
        E = []
        E.append((1, 1))
        for i in range(0, self.p):
            e = self._get_y(i)
            if e is not None:
                E.append((i, e[0]))
                E.append((i, e[1]))
        return E

def main():
    cryptoProvider = ECCryptoProvider()

    # He mat 1
    r1 = cryptoProvider.generate_cryptographic()
    print('-' * 50)
    
if __name__ == '__main__':
    main()
