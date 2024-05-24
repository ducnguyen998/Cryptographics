import CryptoAlgorithms as crypto
import PrimeHelper as primeHelper
import random as rd

_bits_min = 1025

### Choose p is a prime

checker = primeHelper.MillerRabinChecker()

_b = False
_i = 0
while _b is False:
    _n = rd.randint(2 ** 2048, 2 ** 4096)
    _b = checker.get_probably_prime(_n, 2 ** 1024)
    _i += 1
    print(f'{_n} is prime : {_b} - {_i}')

print(f'{_n} is prime : {_b}')

### Create Z*p

### Choose a in Z*p

#a = rd.randint(_n / 2, _n - 1)
#print (a)

### K' = a

### Find K" = (p, alpha, beta)

### - alpha : 

### - beta  : alpha^a mode p