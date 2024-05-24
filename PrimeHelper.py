
#
## Miller-Rabin algorithm
#

import random

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
        
