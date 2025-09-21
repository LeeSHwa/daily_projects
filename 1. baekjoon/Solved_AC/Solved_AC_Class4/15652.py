# https://www.acmicpc.net/problem/15652

# 문제 - N과 M (4)

# 백트래킹

N, M = map(int, input().split())

line = []

def backtrack(start):
    
    if len(line) == M:
        print(" ".join(map(str, line)))
        return
    
    for i in range(start, N+1):
        line.append(i)
        backtrack(i)
        line.pop()

backtrack(1)