import random

# Extended Euclidean Algorithm for finding modular inverse
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Modular Inverse
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
    
# Fast modular exponentiation
def fast_mod_exp(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result

# Generate large prime number
def generate_prime(bits_min=4, bits_max=5):
    # A simple method to generate a prime number for educational purpose
    while True:
        p = random.randint(2**bits_min, 2**bits_max)  # 5-bit prime
        if all(p % i != 0 for i in range(2, int(p**0.5) + 1)):
            return p