n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

visited = [[False] * m for _ in range(n)]

dirs = [(1, 0), (0, 1)]

def dfs(row, col):

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and edges[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)

dfs(0, 0)

if visited[n - 1][m - 1] == True:
    print(1)
else:
    print(0)
    
    
