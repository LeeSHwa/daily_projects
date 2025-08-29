# https://www.acmicpc.net/problem/7569

# 문제 - 토마토 (3차원)
from collections import deque

M, N, H = map(int, input().split())

queue = deque()
tomato_box = []

unripe_tomatos = 0 # 안익은 토마토 개수

visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(H):
    layer = []

    for j in range(N):
        row_data = list(map(int, input().split()))
        
        for k, value in enumerate(row_data):
            if value == 1:
                queue.append((i, j, k, 0)) # 익은 토마토 발견시 바로 queue에 집어넣음
                visited[i][j][k] = True    # queue에 넣는 순간 visited 처리

            elif value == 0:
                unripe_tomatos += 1        # 0이라면 안익은 토마토 개수 += 1

        layer.append(row_data)

    tomato_box.append(layer)

if unripe_tomatos == 0: # 엣지케이스 처리
    print(0)
    exit()

direction = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]

max_day = 0

while queue:
    height, row, col, day = queue.popleft()
    max_day = max(day, max_day)

    for dh, dr, dc in direction:
        nh = height + dh
        nr = row + dr
        nc = col + dc

        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not visited[nh][nr][nc] and tomato_box[nh][nr][nc] == 0:
            queue.append((nh, nr, nc, day + 1))
            visited[nh][nr][nc] = True
            unripe_tomatos -= 1

if unripe_tomatos > 0: # 만약 안익은 토마토가 1개 이상이라면
    print(-1)          # 예외처리
    exit()

print(max_day)