# https://www.acmicpc.net/problem/15663

# 문제 - N과 M (9)
import sys

print = sys.stdout.write

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))
visited = [False] * N
line = []
# set_list = set()

def BackTracking():
    if len(line) == M:
        # if tuple(line) in set_list:
        #     return
        # set_list.add(tuple(line))
        print(" ".join(map(str, line)) + "\n")
        return
    
    prev_num = 0
    for i in range(N):
        if not visited[i] and prev_num != nums[i]:

            visited[i] = True
            line.append(nums[i])
            prev_num = nums[i]
            
            BackTracking()

            line.pop()
            visited[i] = False

BackTracking()