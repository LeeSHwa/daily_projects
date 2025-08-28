# https://www.acmicpc.net/problem/7576

# 문제 - 토마토
from collections import deque

M, N = map(int, input().split()) # M : 가로, M : 세로

tomato = []
start_list = []


for i in range(N):
    line = list(map(int, input().split()))
    count = 0

    for j in line:
        if j == 1:
            start_list.append((i, count))

        count += 1
    tomato.append(line)


def bfs(list):
    queue = deque()
    for start_row, start_column in list:
        queue.append((start_row, start_column, 0))

    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    maximum_depth = 0
    visited = [[False] * M for _ in range(N)]

    while queue:
        row, col, depth = queue.popleft()
        # tomato[row][col] = min(depth + 1, tomato[row][col])
        tomato[row][col] = depth
        maximum_depth = max(maximum_depth, depth)

        for dr, dc in direction:
            nr = row + dr
            nc = col + dc 
            
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and tomato[nr][nc] != -1:

                    queue.append((nr, nc, depth + 1))
                    visited[nr][nc] = True
                
                elif visited[nr][nc] and tomato[nr][nc] > depth + 1:
                    queue.append((nr, nc, depth + 1))

    
    return maximum_depth

answer = float('inf')
answer = min(bfs(start_list), answer)

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit()

print(answer)