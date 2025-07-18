from collections import defaultdict, deque

N = int(input())
T = int(input())

graph = defaultdict(list)

for i in range(T):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        # if current not in visited:
        #     visited.add(current)
        #     queue.extend([neighbor for neighbor in graph[current] if neighbor not in visited])
    
    return visited

visited = bfs(1)

print(len(visited) - 1)