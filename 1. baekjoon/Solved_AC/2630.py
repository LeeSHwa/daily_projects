# https://www.acmicpc.net/problem/2630

# 문제 - 색종이 만들기

N = int(input())

array = [[0]*N for _ in range(N)]


for i in range(N):
    for j in range(N):
        print(array[i][j], end = ' ')
    print()

