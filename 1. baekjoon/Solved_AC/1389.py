# https://www.acmicpc.net/problem/1389
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

friends = defaultdict(set)

N, M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

def bfs(start):
    visited = set([start])
    queue = deque([(start, 0)]) # 숫자, depth
    total_distance = 0

    while queue:
        current, depth = queue.popleft()
        total_distance += depth

        for next_node in friends[current]:
            if next_node not in visited:
                queue.append((next_node, depth + 1))
                visited.add(next_node)
    
    return total_distance

min_bacon = float('inf')
answer = -1
for i in range(1, N+1):
    distance = bfs(i)
    if distance < min_bacon or (distance == min_bacon and i < answer):
        min_bacon = distance
        answer = i

print(answer)