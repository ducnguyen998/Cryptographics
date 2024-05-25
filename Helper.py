
#
## Miller-Rabin algorithm
#

import random
import math

class MillerRabinChecker:  
    def get_probably_prime(self, n, k):
        #
        if n == 2 or n == 3:
            return True
        if n <= 1 or n % 2 == 0:
            return False
        # n-1 --> 2^s * d
        s = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            s += 1
        #
        for _ in range(k):
            a = random.randint(2, n - 2)
            if self.is_composite(a, n, d, s):
                return False
        return True
    def is_composite(self, a, n, d, s):
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            return False
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True
        
class PrimeHelper:
    def __init__(self):
        self._checker = MillerRabinChecker()
    def create(self, bits_min=1024, bits_max=2048, k=64):
        _b = False
        _i = 0
        while _b is False:
            _n = random.randint(2 ** bits_min, 2 ** bits_max)
            _b = self._checker.get_probably_prime(_n, k)
            _i += 1
        print(f'{_n} is prime : {_b} - {_i}')
        return _n
    def _prime_factors(self, n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        if n > 2:
            factors.add(n)
        return factors
    def _is_primitive_root(self, g, p):
        p_minus_1 = p - 1
        factors = self._prime_factors(p_minus_1)
        for factor in factors:
            if pow(g, p_minus_1 // factor, p) == 1:
                return False
        return True
    def find_primitive_root(self, p):
        # be sure p is a prime
        for g in range(2, p):
            if self._is_primitive_root(g, p):
                return g
        return None
    def modular_exponentiation(self, base, exponent, modulus):
        '''
        Return : base ** exponent % modulus
        '''
        result = 1
        base = base % modulus  # Nếu base >= modulus

        while exponent > 0:
            if (exponent % 2) == 1:  # Nếu exponent là số lẻ
                result = (result * base) % modulus
            exponent = exponent >> 1  # Chia exponent cho 2
            base = (base * base) % modulus

        return result
    #
    #
    #
    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = self.extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    def mod_inverse(self, a, p):
        gcd, x, _ = self.extended_gcd(a, p)
        if gcd != 1:
            return None #raise ValueError(f"{a} không có số nghịch đảo modulo {p}")
        else:
            return x % p
    #
    #
    #
    def find_co_prime(self, m):
        e = 2
        while math.gcd(m, e) != 1:
            e += 1
        return e