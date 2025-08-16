# https://www.acmicpc.net/problem/2667

# 문제 - 단지번호붙이기
from collections import deque

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x ,start_y))

    visited[start_x][start_y] = True
    count = 1

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    
    return count

answer = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            answer.append(bfs(i, j))

print(len(answer))

answer.sort()

print('\n'.join(map(str, answer)))