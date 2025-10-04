# https://www.acmicpc.net/problem/15649

# 문제 - N과 M (1)

# 1 <= M <= N <= 8
# 1부터 N까지 자연수 중 중복없이 M개를 고른 수열

N, M = map(int, input().split())

nums = [x for x in range(1, N+1)]

line = []

def BactTrack():
    if len(line) == M:
        print(" ".join(map(str, line)))
        return
    
    for i in range(N):
        if nums[i] in line:
            continue
        
        line.append(nums[i])
        BactTrack()
        line.pop()

BactTrack()