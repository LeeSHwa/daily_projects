# 그냥 무조건 0, 0에서 시작해서 닿는 1들의 위치만 따로 기록함 to_melt
# 그 다음에 to_melt만 녹이는거지, cnt 올리고
# 한 번 쫙 순회하면서 1 몇 개 있는 지 기록도 하고.

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def bfs(shell):
    to_melt = []
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    q.append((cnt, cnt))
    visited = [[False] * m for _ in range(n)]

    while q:
        row, col = q.popleft()
        
        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc

            if shell <= nr < n - shell and shell <= nc < m - shell and not visited[nr][nc]:
                if grid[nr][nc] == 1:
                    to_melt.append((nr, nc))
                
                else:
                    q.append((nr, nc))
                
                visited[nr][nc] = True
        
    return to_melt

last = -1
cnt = 0

while True:
    array = bfs(cnt)
    
    if len(array) == 0:
        print(cnt, last)
        break
    
    for r, c in array:
        grid[r][c] = 0
    
    last = len(array)
    cnt += 1
