import math

def is_prime(N):
    sqrt_N = math.sqrt(N)

    for i in range(2, sqrt_N + 1):
        if N % i == 0:
            return False

    return True

A, B = map(int, input().split())