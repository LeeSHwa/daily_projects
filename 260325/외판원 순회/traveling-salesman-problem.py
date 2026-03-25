n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

# 0은 True로 해둘까?
visited = [False] * n
min_price = float('inf')

def backtrack(start, explored_cnt, curr_price):
    global min_price

    if curr_price > min_price:
        return

    if explored_cnt == n:
        total_price = curr_price + grid[start][0]
        min_price = min(min_price, total_price)
        return
    
    for end in range(n):
        if end == start or visited[end]:
            continue
        
        visited[end] = True
        
        backtrack(end, explored_cnt + 1, curr_price + grid[start][end])

        visited[end] = False

backtrack(0, 0, 0)

print(min_price)