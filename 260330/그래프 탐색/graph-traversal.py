from collections import defaultdict

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

array = defaultdict(list)

for start, end in edges:
    array[start].append(end)
    array[end].append(start)
    

visited = [False] * (n + 1)

ans = 0

def dfs(num, cnt):
    global ans

    ans = max(cnt, ans)
    
    visited[num] = True
    
    for next_num in array[num]:
        if array[next_num] and not visited[next_num]:
            dfs(next_num, cnt + 1)
    return


dfs(1, 0)

print(ans)