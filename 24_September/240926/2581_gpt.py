import math

def sieve_of_eratosthenes(max_num):
    sieve = [True] * (max_num + 1)  # 처음엔 모두 소수로 가정
    sieve[0], sieve[1] = False, False  # 0과 1은 소수가 아님

    # 2부터 sqrt(max_num)까지의 수에 대해 소수 판별
    for i in range(2, int(math.sqrt(max_num)) + 1):
        if sieve[i]:  # i가 소수라면
            # i의 배수들은 소수가 아니므로 False로 설정
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # True로 남아있는 값들이 소수
    return [x for x in range(2, max_num + 1) if sieve[x]]

# 입력 처리
M = int(input())
N = int(input())

# 에라토스테네스의 체로 N까지의 소수 구하기
primes = [p for p in sieve_of_eratosthenes(N) if p >= M]  # M 이상 N 이하의 소수만 필터링

# 결과 출력
if primes:
    print(sum(primes))  # 소수들의 합
    print(min(primes))  # 가장 작은 소수
else:
    print(-1)
