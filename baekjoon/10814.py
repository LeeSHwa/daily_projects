# https://www.acmicpc.net/problem/10814

N = int(input())
di = {}

for i in range(N):
    key, value = input().split()
    di[key] = value

ans = sorted(di)

for key, value in di.items():
    print(f"{key} {value}")