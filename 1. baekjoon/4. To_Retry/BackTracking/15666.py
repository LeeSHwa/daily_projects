# https://www.acmicpc.net/problem/15666

# 문제 - N과 M (12)

N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))

line = []

N = len(nums)

def BackTracking(current):
    if len(line) == M:
        print(" ".join(map(str, line)))
        return
    
    for i in range(current, N):
        line.append(nums[i])
        BackTracking(i)
        line.pop()

BackTracking(0)