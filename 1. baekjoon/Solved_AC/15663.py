# https://www.acmicpc.net/problem/15663

# 문제 - N과 M (9)

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

line = []

visited = set()

def backtrack():
    if len(line) == M:        

        if tuple(line) in visited:
            return
        else:
            print(' '.join(map(str, line)))

        return
    
    for i in range(N):
        line.append(nums[i])
        backtrack()
        visited.add(tuple(', '.join(map(str, line))))
        line.pop()

backtrack()