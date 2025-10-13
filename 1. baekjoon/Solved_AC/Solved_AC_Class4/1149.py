# https://www.acmicpc.net/problem/1149

# 문제 - RGB거리
from collections import defaultdict

N = int(input())

graph = defaultdict(list)
DP = defaultdict(list)

for i in range(1, N+1):
    graph[i] = list(map(int, input().split()))

DP[1] = graph[1]

depth = 2
while True:
    if depth > N:
        print(min(DP[N]))
        exit()
    DP[depth] = [ graph[depth][0] + min(DP[depth-1][1], DP[depth-1][2]), graph[depth][1] + min(DP[depth-1][0], DP[depth-1][2]), graph[depth][2] + min(DP[depth-1][0], DP[depth-1][1]) ]
    depth += 1

### 아래는 DFS로 구현했을 때의 모습, N이 20보다 커지기만 해도 시간초과가 난다. 이런 경우 무조건 DP를 고려할 것

# DP[depth-1][0] + min(graph[depth][1], graph[depth][2])
# DP[depth-1][1] + min(graph[depth][0], graph[depth][2])
# DP[depth-1][2] + min(graph[depth][0], graph[depth][1])

# import sys

# sys.setrecursionlimit(10**6)

# N = int(input())

# graph = defaultdict(list)

# for i in range(1, N+1):
#     graph[i] = list(map(int, input().split()))

# depth = 1
# subtotal = 0
# answer = float("inf")

# def DFS(subtotal, depth, prev):
#     global answer
#     if depth > N:
#         answer = min(answer, subtotal)
#         return

#     nums = graph[depth]

#     if prev == 0:
#         DFS(subtotal + nums[1], depth + 1, 1)
#         DFS(subtotal + nums[2], depth + 1, 2)

#     elif prev == 1:
#         DFS(subtotal + nums[0], depth + 1, 0)
#         DFS(subtotal + nums[2], depth + 1, 2)

#     else:
#         DFS(subtotal + nums[0], depth + 1, 0)
#         DFS(subtotal + nums[1], depth + 1, 1)

# for i in range(3):
#     subtotal = graph[1][i]
#     DFS(subtotal, depth + 1, i)

# print(answer)