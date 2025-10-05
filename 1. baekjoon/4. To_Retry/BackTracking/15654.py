# https://www.acmicpc.net/problem/15654

# 문제 - N과 M (5)

# N개의 자연수 중 M개를 고른수열
# 입력으로 주어지는 자연수는 10,000보다 작거나 같은 자연수
# print는 sys.stdout.write

# 출력은 사전 순으로 증가하는 순서 (오름차순)
import sys
print = sys.stdout.write

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

line = []
visited = [False] * N

def BackTracking():
    if len(line) == M:
        print(" ".join(map(str, line)) + '\n')
        return

    for i in range(N):
        # if nums[i] in line:
        #     continue

        if visited[i]:
            continue

        visited[i] = True
        line.append(nums[i])

        BackTracking()

        line.pop()
        visited[i] = False

BackTracking()