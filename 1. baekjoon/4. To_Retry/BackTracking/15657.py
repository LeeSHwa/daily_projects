# https://www.acmicpc.net/problem/15657

# 문제 - N과 M (8)

# N개의 자연수 중 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
import sys
print = sys.stdout.write

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

line = []

def BackTracking(start):
    if len(line) == M:
        print(" ".join(map(str, line)) + "\n")
        return
    
    for i in range(start, N):
        line.append(nums[i])
        BackTracking(i)
        line.pop()

BackTracking(0)