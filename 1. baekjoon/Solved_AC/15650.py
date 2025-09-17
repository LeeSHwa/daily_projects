# https://www.acmicpc.net/problem/15650

# 문제 - N과 M(2)
import itertools

N, M = map(int, input().split())

list_N = [x+1 for x in range(N)]
str_N = map(str, list_N)

# result = list(itertools.combinations(list_N, M))

# for line in result:
#     str_result = map(str, line)
#     print(" ".join(str_result))

# 백트래킹

line = []
def backtrack(start, depth, line):
    
    for i in range(start, N+1):
        line.append(i)

        if depth == M:
            print(" ".join(line))
            line.pop()
    
        backtrack(i+1, depth + 1, line)
        line.pop()

backtrack(1, 1, line)