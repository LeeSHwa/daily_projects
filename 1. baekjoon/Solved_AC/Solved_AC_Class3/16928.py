# https://www.acmicpc.net/problem/16928

# 문제 - 뱀과 사다리 게임
from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)

force_move = {}

for _ in range(N+M):
    x, y = map(int, input().split())
    force_move[x] = y


for i in range(1, 100):
    for num in range(1, 7):
        if i + num <= 100:
            if i + num in force_move.keys():
                graph[i].append(force_move[i+num])
                continue
            else:                
                graph[i].append(i + num)

queue = deque([(1, 0)])

answer = []
visited = [False] * 101 
flag = False

while queue:
    start, count = queue.popleft()

    if flag:
        break

    for destination in graph[start]:
        if destination == 100:
            answer = count + 1
            flag = True
            continue
            
        elif not visited[destination]:
            queue.append((destination, count + 1))
            visited[destination] = True
        
print(answer)