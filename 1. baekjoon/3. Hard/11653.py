'''정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.'''
# 간단 버전
# import math

# N = int(input())

# M = int(math.sqrt(N)) + 1

# for i in range(2, N):
#     while N % i == 0:
#         print(i)
#         N //= i
    
# if N > 1:
#     print(N)

N = int(input())

def findPrimeNumber(N):    
    is_prime = [True] * (N + 1)

    is_prime[0] = is_prime[1] = False

    for i in range(2, int(N**0.5 + 1)):
        if is_prime[i]:
            for j in range(i * i, (N + 1), i):
                is_prime[j] = False
    
    primes = [x for x, prime in enumerate(is_prime) if prime]

    return primes
    
if N == 1:
    exit()
else:
    primes = findPrimeNumber(int(N**0.5))
    for p in primes:
        while N % p == 0:
            print(p)
            N //= p
    
    if N > 1:
        print(N)