import random


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def generate_random_prime():
    prime = False
    while not prime:
        p = random.randint(3, 1000)
        prime = is_prime(p)
    return p

def power(a, b, m):
    return (pow(a,b)) % m