# https://www.acmicpc.net/problem/21736

# 문제 - 헌내기는 친구가 필요해
from collections import deque

N, M = map(int, input().split())

campus = []
queue = deque()

# visited = [[False] * M] * N # shallow copy 버그 생김
visited = [[False] * M for _ in range(N)]


for i in range(N):
    row = list(input().strip())
    campus.append(row)

    if 'I' in row:
        pos_x = i
        pos_y = row.index('I')
        
queue.append((pos_x, pos_y))

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(x, y):    
    count = 0
    visited[x][y] = True
    
    while queue:
        px, py = queue.popleft()

        for dx, dy in direction:
            tx = px + dx
            ty = py + dy

            if 0 <= tx < N and 0 <= ty < M and not visited[tx][ty]:

                if campus[tx][ty] in ('P', 'O'):
                    queue.append((tx, ty))
                    visited[tx][ty] = True

                    if campus[tx][ty] == 'P':
                        count += 1
    return count

count = bfs(pos_x, pos_y)

if count == 0:
    print("TT")
else:
    print(count)