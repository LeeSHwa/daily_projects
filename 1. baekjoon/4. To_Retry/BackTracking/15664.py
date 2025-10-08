# https://www.acmicpc.net/problem/15664

# 문제 - N과 M (10)

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

line = []

def BackTracking(current):
    if len(line) == M:
        print(" ".join(map(str, line)))
        return
    
    prev = 0
    for i in range(current, N):
        if nums[i] == prev:
            continue

        line.append(nums[i])
        prev = nums[i]

        BackTracking(i+1)

        line.pop()

BackTracking(0)