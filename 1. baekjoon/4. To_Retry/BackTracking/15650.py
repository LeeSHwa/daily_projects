# https://www.acmicpc.net/problem/15650

# 문제 - N과 M (2)

# 1부터 N까지 자연수 중에 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순 이여야 함

# 1 <= M <= N <= 8

N, M = map(int, input().split())

nums = [x for x in range(1, N + 1)]

line = []

def BackTracking():
    if len(line) == M:
        print(" ".join(map(str, line)))
        return
    
    for i in range(N):
        if line and nums[i] <= line[-1]:
            continue
        
        line.append(nums[i])
        BackTracking()
        line.pop()

BackTracking()