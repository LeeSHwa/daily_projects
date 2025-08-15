from collections import defaultdict, deque
import sys

input = sys.stdin.readline

friends = defaultdict(set)

N, M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

def bfs(start):
    queue = deque([(start, 0)])
    visited = {start}
    total_distance = 0
    
    while queue:
        current, depth = queue.popleft()
        total_distance += depth

        for next_node in friends[current]:
            if next_node not in visited:
                queue.append((next_node, depth + 1))
                visited.add(next_node)
    
    return total_distance

min_bacon_value = float('inf')
min_bacon_person = -1

for i in range(1, N+1):
    current_distance = bfs(i)
    if current_distance < min_bacon_value:
        min_bacon_value = current_distance
        min_bacon_person = i

print(min_bacon_person)