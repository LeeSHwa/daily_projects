from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

starts = [tuple(map(int, input().split())) for _ in range(k)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = []

possible_vertexs = set()

def refresh_visited():
    global visited
    visited = [[False] * n for _ in range(n)]

def can_go(row, col):
    if row >= n or row < 0 or col >= n or col < 0:
        return False
    
    if visited[row][col]:
        return False
    
    if grid[row][col]:
        return False
    
    return True


def bfs():
    # global possible_vertexs
    for r, c in starts:
        refresh_visited()

        q = deque()

        r -= 1
        c -= 1

        q.append((r, c))
        
        while q:
            row, col = q.popleft()

            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if can_go(nr, nc):
                    visited[nr][nc] = True
                    possible_vertexs.add((nr, nc))
                    q.append((nr, nc))

bfs()
print(len(possible_vertexs))




    
    