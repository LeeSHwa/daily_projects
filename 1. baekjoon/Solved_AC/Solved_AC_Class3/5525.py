# https://www.acmicpc.net/problem/5525

# 문제 - IOIOI
import sys
from collections import deque

input = sys.stdin.readline

# Pn
N = int(input())

# 문자열 S의 길이
M = int(input())

S = input().strip()

pattern_count = 0
i = 0
count = 0

while i < M - 2:
    if S[i:i+3] == 'IOI':
        pattern_count += 1
        i += 2

        if pattern_count >= N:
            count += 1
        

    else:
        pattern_count = 0
        i += 1

print(count)