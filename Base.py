from enum import (
    Enum
)

from Helper import (
    PrimeHelper
)


class ECrypto(Enum):
    RSA = 0
    ElGamal = 1
    EllipticCurve = 2

class SharableKeyCryptographic:
    def __init__(self, K_i, K_ii):
        # Public key
        self.K_i = K_i
        # Private key
        self.K_ii = K_ii
        # Helper
        self.helper = PrimeHelper()
    def encrypt(self, x):
        pass
    def decrypt(self, y):
        pass
    def encrypt_by_partner(self, x, K_i_partner):
        pass
    def decrypt_by_partner(self, y, K_ii_partner, p):
        pass