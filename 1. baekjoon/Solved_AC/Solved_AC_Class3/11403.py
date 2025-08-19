# https://www.acmicpc.net/problem/11403

# 문제 - 경로 찾기
from collections import defaultdict, deque

N = int(input())
matrix = []
graph = defaultdict(list)

for i in range(N):
    line = list(map(int, input().split()))
    matrix.append(line)
    
    for j in range(len(line)):
        if line[j] == 1:
            graph[i].append(j)

for row in range(N):
    queue = deque()
    queue.append(row)
    visited = set()
    
    ans_line = ['0'] * N

    while queue:
        current = queue.popleft()
        
        for next_node in graph[current]:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
                ans_line[next_node] = '1'
        
    print(' '.join(ans_line))
