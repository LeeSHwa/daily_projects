# https://www.acmicpc.net/problem/15665

# 문제 - N과 M (11)

# 1 <= M <= N <= 7

# 같은 수를 여러 번 골라도 된다.

N, M = map(int, input().split())

nums = sorted(list(set(map(int, input().split()))))

line = []

N = len(nums) # 굳이 중복되는 번호를 신경쓸 필요 없게 갱신

def BackTracking():
    if len(line) == M:
        print(" ".join(map(str, line)))
        return

    for i in range(N):
        line.append(nums[i])
        BackTracking()
        line.pop()

BackTracking()

