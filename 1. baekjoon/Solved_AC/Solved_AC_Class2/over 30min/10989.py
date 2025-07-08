# https://www.acmicpc.net/problem/10989

import sys

count = [0 for X in range(10001)]

N = int(input())

for i in range(N):
    # array.append(int(sys.stdin.readline()))
    n = int(sys.stdin.readline())
    count[n] += 1

for j in range(10001): 
    if count[j] != 0:
        while count[j] > 0:
            print(j)
            count[j] -= 1