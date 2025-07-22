import math

N = int(input())

M = int(math.sqrt(N)) + 1

for i in range(2, N):
    while N % i == 0:
        print(i)
        N //= i
    
if N > 1:
    print(N)