import random as rd

from Helper import (
    PrimeHelper
)

from Base import (
    SharableKeyCryptographic
)

class ElGamalCryptoProvider:

    def __init__(self):
        self.helper = PrimeHelper()

    def generate_cryptographic(self, bm=16, bM=17):
        p = self.helper.create(bits_min=bm, bits_max=bM, k=64)
        #print(f'p={p}')
        a = p - rd.randint(2 ** (bm-2), 2 ** (bm-1))
        #print(f'a={a}')
        #
        K_ii = a
        #
        alpha = self.helper.find_primitive_root(p)
        #print(f'alpha={alpha}')
        beta  = self.helper.modular_exponentiation(alpha, a, p)
        #print(f'beta={beta}')
        #
        K_i = (p, alpha, beta)
        # 
        return ElGamalCrypto(K_i, K_ii)

class ElGamalCrypto(SharableKeyCryptographic):
    def __init__(self, K_i, K_ii):
        super().__init__(K_i, K_ii)
        self.a = K_ii
        self.p, self.alpha, self.beta = K_i
    #
    # Encrypt by self.K_i (public key)
    #
    def encrypt(self, x):
        p, alpha, beta = self.p, self.alpha, self.beta
        k = rd.randint(2, self.p - 1)
        c1 = self.helper.modular_exponentiation(alpha, k, p)
        c2 = self.helper.modular_exponentiation( beta, k, p) * x % p
        return c1, c2
    #
    # Decrypt by partner K_ii & p 
    #
    def decrypt(self, y):
        a = self.a
        p = self.p
        c1, c2 = y
        x = c2 * self.helper.mod_inverse(c1 ** a, p) % p
        return x
    
    #
    # Encrypt by partner K_i (public key)
    #
    def encrypt_by_partner(self, x, K_i_partner):
        p, alpha, beta = K_i_partner
        k = rd.randint(2, self.p - 1)
        c1 = self.helper.modular_exponentiation(alpha, k, p)
        c2 = self.helper.modular_exponentiation( beta, k, p) * x % p
        return c1, c2
    
    #
    # Decrypt by partner K_ii & p 
    #
    def decrypt_by_partner(self, y, K_ii_partner, p_partner):
        a = K_ii_partner
        p = p_partner
        c1, c2 = y
        x = c2 * self.helper.mod_inverse(c1 ** a, p) % p
        return x
    
    def __str__(self) -> str:
        return f'ElGamalCrypto: K_i = [p={self.p}, alpha={self.alpha}, beta={self.beta}], K_ii = [a={self.a}]'

class ElGamalCryptoSignature:
    def __init__(self, crypto):
        self.crypto = crypto
        self.a = self.crypto.K_ii
        self.p, self.alpha, self.beta = self.crypto.K_i

        # Choose a k value, that have inverse value in mod(p-1)
        for i in range(2, self.p - 1):
            if self.crypto.helper.mod_inverse(i, self.p - 1) != None:
                self.k = i
                break

        if self.k is None:
            raise ValueError(f"self.k is None")

        self.gamma = self.crypto.helper.modular_exponentiation(self.alpha, self.k, self.p)

    def sign(self, x):
        self.delta = (x - self.a * self.gamma) * self.crypto.helper.mod_inverse(self.k, self.p - 1) % (self.p - 1)
        print(f'Sign : (hx, (gamma, delta)) = ({x},({self.gamma}, {self.delta}))')
    def verify(self, x, y, K_i_partner):
        gamma, delta = y
        p, alpha, beta = K_i_partner
        v1 = self.crypto.helper.modular_exponentiation((beta ** gamma) * (gamma ** delta), 1, p)
        v2 = self.crypto.helper.modular_exponentiation(alpha, x, p)
        print(f'v1={v1}, v2={v2}')
        return v1 == v2

def main():
    cryptoProvider = ElGamalCryptoProvider()

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
    s1 = ElGamalCryptoSignature(r1)
    s2 = ElGamalCryptoSignature(r2)

    s2.sign(x)
    verify = s2.verify(x, (s2.gamma, s2.delta), s2.crypto.K_i)
    print(f'verification : {verify}')

if __name__ == '__main__':
    main()