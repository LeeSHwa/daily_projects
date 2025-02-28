# https://www.acmicpc.net/problem/1436

N = int(input())

temp = []

for i in range(666,2670000):
    if '666' in str(i):
        temp.append(i)

ans = sorted(temp)

print(ans[N-1])
