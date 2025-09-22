# https://www.acmicpc.net/problem/15654

# 문제 - N과 M (5)

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

line = []

def backtrack():
    
    if len(line) == M:
        print(" ".join(map(str, line)))
        return

    for i in range(N):
        if nums[i] in line:
            continue
        line.append(nums[i])
        backtrack()
        line.pop()

backtrack()