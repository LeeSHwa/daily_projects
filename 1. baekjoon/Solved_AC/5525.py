# https://www.acmicpc.net/problem/5525

import sys
from collections import deque

input = sys.stdin.readline

# Pn
N = int(input())

Pn = ['I']
Pn.extend('OI' * N)

# 문자열 S의 길이
M = int(input())

S = list(input().strip())
len_S = len(S)

start = 0
end = 2*N + 1

count = 0

current = deque(S[start : end])
print(current)

while end != len(S) + 1:


    # if slicing == Pn:
        # count += 1

    for i in range(2 * N + 1):
        if S[start + i] != Pn[i] and not flag:
            flag = True
            break

    start += 1
    end += 1
print(count)