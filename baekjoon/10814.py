# https://www.acmicpc.net/problem/10814

N = int(input())
di = {}

for i in range(N):
    key, value = input().split()
    di[key] = value

# def sort_di(di):
    # while f



for key, value in di.items():
    print(f"{key} {value}")