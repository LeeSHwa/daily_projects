# https://www.acmicpc.net/problem/14940

# 문제 - 쉬운 최단거리
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
visited = [[False] * M for _ in range(N)]

for i in range(N):
    line = list(map(int, input().strip().split()))

    if 2 in line:
        col = line.index(2)
        row = i

    matrix.append(line)

def bfs(row, col):
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    depth = 0
    queue = deque([(row, col, depth)])

    while queue:
        r, c, dep = queue.popleft()
        matrix[r][c] = dep

        for dr, dc in dir:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < N and 0 <= nc < M and matrix[nr][nc] == 1 and not visited[nr][nc]:
                queue.append((nr, nc, dep + 1))
                visited[nr][nc] = True

bfs(row, col)

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1 and not visited[i][j]:
            print(-1, end = " ")
        else:
            print(matrix[i][j], end = " ")
    print()