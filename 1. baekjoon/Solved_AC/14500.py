# https://www.acmicpc.net/problem/14500

# 문제 - 테트로미노

N, M = map(int, input().split())
grid = []

for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

visited = [[False] * M for _ in range(N)]

max_sum = 0

def DFS(col, row, depth, current_sum):
    global max_sum

    if depth == 4:
        max_sum = max(max_sum, current_sum)
        return # 백트래킹

    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    for dc, dr in direction:
        nc = col + dc
        nr = row + dr

        if not (0 <= nc < N and 0 <= nr < M) or visited[nc][nr]:
            continue
    
        visited[nc][nr] = True
        DFS(nc, nr, depth + 1, current_sum + grid[nc][nr])

        visited[nc][nr] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, grid[i][j])
        visited[i][j] = False

        dc = [(0, 1), (0, -1)]
        dr = [(1, 0), (-1, 0)]

        
        

