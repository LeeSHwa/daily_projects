# https://www.acmicpc.net/problem/14500

# 문제 - 테트로미노

N, M = map(int, input().split())
grid = []

for _ in range(N):
    line = list(map(int, input().split()))
    grid.append(line)

stack = []

visited = [[False] * M for _ in range(N)]

def DFS(col, row, depth, current_sum):

    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    
    for dcol, drow in direction:
        ncol = col + dcol
        nrow = row + drow

        