# https://www.acmicpc.net/problem/14500

# 문제 - 테트로미노

N, M = map(int, input().split())
grid = []

max_value_in_grid = -1
max_sum = -1

for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)
    max_value_in_grid = max(max_value_in_grid, max(line))

visited = [[False] * M for _ in range(N)]

def DFS(row, col, depth, current_sum):
    global max_sum

    if depth < 4 and max_sum > current_sum + (4 - depth) * max_value_in_grid:
        return

    if depth == 4:
        max_sum = max(max_sum, current_sum)
        return
    
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    for dr, dc in direction:
        nr = row + dr
        nc = col + dc

        if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc]:
            continue
        

        visited[nr][nc] = True
        DFS(nr, nc, depth + 1, current_sum + grid[nr][nc])
        visited[nr][nc] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, 1, grid[i][j])
        visited[i][j] = False

        neighbors = []

        if i > 0: neighbors.append(grid[i-1][j])
        if i + 1 < N: neighbors.append(grid[i+1][j])
        if j > 0: neighbors.append(grid[i][j-1])
        if j + 1 < M: neighbors.append(grid[i][j+1])

        if len(neighbors) >= 3:
            neighbors.sort(reverse=True)
            max_sum = max(max_sum, grid[i][j] + sum(neighbors[:3]))

print(max_sum)            