# https://www.acmicpc.net/problem/11050

# import math

# N, K = map(int,input().split())

# print(int( math.factorial(N) / ( math.factorial(K) * math.factorial(N-K) ) ))


def facto(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    
    temp = num
    
    return facto(num-1)*temp


N, K = map(int,input().split())

print(int(facto(N) / (facto(K) * facto(N-K)) ) )