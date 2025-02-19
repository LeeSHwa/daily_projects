# https://www.acmicpc.net/problem/10989

k = 1000000

count = [0 for X in range(k)]
temp = []
array = []
N = int(input())

for i in range(N):
    array.append(int(input()))    

for j in array:
    count[j] += 1

for k in range(N):
    if count[k] != 0:
        for l in range(count[k]):
            print(k)