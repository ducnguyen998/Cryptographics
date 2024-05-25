from Helper import (
    PrimeHelper
)

from Base import (
    SharableKeyCryptographic
)

class RSACryptoProvider:
    def __init__(self):
        self.helper = PrimeHelper()

    def generate_cryptographic(self, bits_min=16, bits_max=17):
        # Choose p, q as primes
        p = self.helper.create(bits_min, bits_max, k=64)
        q = self.helper.create(bits_min, bits_max, k=64)
        # Calculate n and m = phi(n)
        n = p * q
        m = p * q - (p + q) + 1 # (p-1)*(q-1)
        # Calculate e : GCD(e,m) = 1
        e = self.helper.find_co_prime(m)
        # Find mod inverse d = e^-1 mod m
        d = self.helper.mod_inverse(e, m)
        # Public key
        self.K_i = (n, e)
        # Private key
        self.K_ii = d

        return RSACrypto(self.K_i, self.K_ii)

class RSACrypto(SharableKeyCryptographic):
    def __init__(self, K_i, K_ii):
        super().__init__(K_i, K_ii)
        self.n, self.e = K_i
        self.d = K_ii
    
    def encrypt(self, x):
        return self.helper.modular_exponentiation(x, self.e, self.n)  
    def decrypt(self, y):
        return self.helper.modular_exponentiation(y, self.d, self.n)
    def encrypt_by_partner(self, x, K_i_partner):
        n, e = K_i_partner
        return self.helper.modular_exponentiation(x, e, n)
    def decrypt_by_partner(self, y, K_ii_partner, p):
        n, d = p, K_ii_partner
        return self.helper.modular_exponentiation(y, d, n)
    
    def __str__(self) -> str:
        return f'RSACrypto: K_i = [n={self.n}, e={self.e}], K_ii = [d={self.d}]'

class RSACryptoSignature:
    def __init__(self, crypto):
        self.crypto = crypto
    
    def sign(self, x):
        y_ = self.crypto.helper.modular_exponentiation(x, self.crypto.e, self.crypto.n)
        self.y = y_
        return y_
    def verify(self, x, y):
        v1 = x
        v2 = self.crypto.helper.modular_exponentiation(y, self.crypto.d, self.crypto.n)
        print(f'v1={v1}, v2={v2}')
        return v1 == v2


def main():
    cryptoProvider = RSACryptoProvider()

    # He mat 1
    r1 = cryptoProvider.generate_cryptographic()
    print(r1)
    print('-' * 50)

    # He mat 2
    r2 = cryptoProvider.generate_cryptographic()
    print(r2)
    print('-' * 50)

    # Crypting

    x = 12345
    y = r1.encrypt_by_partner(x, r1.K_i)
    m = r1.decrypt(y)
    print(f'x={x} : encrypt({y}) , decrypt({m})')

    # Signature
    s1 = RSACryptoSignature(r1)
    s2 = RSACryptoSignature(r2)

    s2.sign(x)
    verify = s2.verify(x, s2.y)
    print(f'verification : {verify}')

if __name__ == '__main__':
    main()