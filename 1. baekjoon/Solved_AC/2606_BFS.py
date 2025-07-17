from collections import defaultdict, deque

N = int(input())
T = int(input())

graph = defaultdict(list)

for i in range(T):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(node, start):
    queue = deque(start)
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend([neighbor for neighbor in graph[node] if neighbor not in visited])
    
    return visited

visited = bfs(graph, 1)

print(len(visited))