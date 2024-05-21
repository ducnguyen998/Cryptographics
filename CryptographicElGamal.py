import CryptoAlgorithms as crypto

_bits_min = 62

### Choose p is a prime

p = crypto.generate_prime(bits_min=_bits_min, bits_max=_bits_min+1)

print(f'{_bits_min} prime : {p}')

### Create Z*p

### Choose a in Z*p

### K' = a

### Find K" = (p, alpha, beta)

### - alpha : 

### - beta  : alpha^a mode p