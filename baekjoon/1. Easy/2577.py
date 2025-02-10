# https://www.acmicpc.net/problem/2577

A = int(input())
B = int(input())
C = int(input())

value = str(A * B * C)

for i in range(0,10):
    cnt = 0
    for j in value:
        if int(j) == i:
            cnt += 1
            pass
    print(cnt)

