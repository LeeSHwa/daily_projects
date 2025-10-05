# https://www.acmicpc.net/problem/15651

# 1부터 N까지 자연수 중 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨

# 1 <= M <= N <= 7

N, M = map(int, input().split())

line = []

def BackTracking():
    if len(line) == M:
        print(" ".join(map(str, line)))
        return

    for i in range(1,N+1):
        line.append(i)
        BackTracking()
        line.pop()

BackTracking()