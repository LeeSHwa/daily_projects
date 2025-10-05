# https://www.acmicpc.net/problem/15652

# 문제 - N과 M (4)

# 1부터 N까지 자연수 중 M개를 고른 수열
# 같은 수를 여러 번 골라도 됨
# 고른 수열은 비내림차순 (= 중복을 허용하는 오름차순)

# 1 <= M <= N <= 8

N, M = map(int, input().split())

line = []

def BackTracking():
    if len(line) == M: 
        print(" ".join(map(str, line)))
        return
    
    for i in range(1, N+1):
        if line and i < line[-1]:
            continue

        line.append(i)
        BackTracking()
        line.pop()

BackTracking()