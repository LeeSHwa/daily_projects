# https://www.acmicpc.net/problem/1929

'''
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1 
3 16
예제 출력 1 
3
5
7
11
13
'''

M, N = map(int, input().split())

# 1. sqrt(N)까지 소수 구하기 (에라토스테네체 적용을 위함)
limit = int(N ** 0.5) + 1
sqrt_prime = [True] * (limit)
sqrt_prime[0] = sqrt_prime[1] = False

for i in range(2, limit):
    if sqrt_prime[i]:
        for j in range(i * i, limit, i):
            sqrt_prime[j] = False

primes = [i for i, val in enumerate(sqrt_prime) if val]

# 2. 위 primes를 활용하여 에라토스테네체 적용
is_prime = [True] * (N - M + 1)
for p in primes:
    start = max(p * 2, ((M + p - 1) // p) * p)
    for j in range(start, N + 1, p):
        is_prime[j - M] = False

if M == 1:
    is_prime[0] = False

for i in range(N - M + 1):
    if is_prime[i]:
        print(i + M)