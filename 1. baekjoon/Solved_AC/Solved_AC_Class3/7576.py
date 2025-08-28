# https://www.acmicpc.net/problem/7576

# 문제 - 토마토
from collections import deque

M, N = map(int, input().split()) # M : 가로, M : 세로

tomato = []
start_list = []

for i in range(N):
    line = list(map(int, input().split()))

    for j, value in enumerate(line):
        if value == 1:
            start_list.append((i, j))

    tomato.append(line)


def bfs(list):
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    maximum_depth = 0

    for start_row, start_column in list:
        queue.append((start_row, start_column, 1))
        visited[start_row][start_column] = True
    

    while queue:
        row, col, depth = queue.popleft()
        tomato[row][col] = depth
        maximum_depth = max(maximum_depth, depth)

        for dr, dc in direction:
            nr = row + dr
            nc = col + dc 
            
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and tomato[nr][nc] != -1:

                    queue.append((nr, nc, depth + 1))
                    visited[nr][nc] = True

    return maximum_depth - 1

answer = bfs(start_list)

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()

print(answer)