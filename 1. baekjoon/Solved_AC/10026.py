# https://www.acmicpc.net/problem/10026

# 문제 - 적록색약
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