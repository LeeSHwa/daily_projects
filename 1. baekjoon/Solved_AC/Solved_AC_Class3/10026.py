# https://www.acmicpc.net/problem/10026

# 문제 - 적록색약
from collections import deque
N = int(input())

grid = []
abnormal_grid = []

for i in range(N):
    line = list(input())
    grid.append(line)
    
    abnormal_line = line.copy()
    for j, color in enumerate(line):
        if color == 'R':
            abnormal_line[j] = 'G'
    
    abnormal_grid.append(abnormal_line)

def bfs(matrix ,start_row, start_col, visited):

    queue = deque([(start_row, start_col, matrix[start_row][start_col])])
    visited[start_row][start_col] = True
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while queue:
        row, col, current_color = queue.popleft()
        
        for dr, dc in direction:
            nr = row + dr
            nc = col + dc
            
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if current_color == matrix[nr][nc]:
                    queue.append((nr, nc, matrix[nr][nc]))
                    visited[nr][nc] = True
        
normal_ans = abnormal_ans = 0

visited = [[False] * N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if not visited[row][col]:
            bfs(grid, row, col, visited)
            normal_ans += 1

visited = [[False] * N for _ in range(N)]
for row in range(N):
    for col in range(N):
        if not visited[row][col]:
            bfs(abnormal_grid, row, col, visited)
            abnormal_ans += 1

print(normal_ans, abnormal_ans)