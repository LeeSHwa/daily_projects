# https://www.acmicpc.net/problem/10989

N = int(input())

temp = [] 
for i in range(N):
    temp.append(input())

ans = sorted(temp)

for j in range(N):
    print(ans[j])