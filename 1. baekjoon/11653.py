'''정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.'''

N = int(input())

def findPrimeNumber(N):

    if N == 1:
        return
    
    primeNumber = set(range(1, N+1))

    for i in range(2, N):
        is_prime = True

        if is_prime:
            while K % i == 0:
                print(i)
                K /= i
                
                if K == 1:
                    break

findPrimeNumber(N)

# while N != 1:
#     for i in divider:
#         while N % i == 0:
#             print(i)
#             N /= i
