# https://www.acmicpc.net/problem/15655

# 문제 - N과 M (6)

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

line = []
# visited = [False] * N

def BackTracking(current):
    if len(line) == M:
        print(' '.join(map(str, line)))
        return
    
    for i in range(current, N):
        # if visited[i] or (line and nums[i] < line[-1]):
        #     continue
        
        # visited[i] = True
        line.append(nums[i])

        BackTracking(i+1)

        line.pop()
        # visited[i] = False

BackTracking(0)