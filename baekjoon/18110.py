# https://www.acmicpc.net/problem/18110
from statistics import mean

n = int(input())

k = round(n*0.15)
li = []

for i in range(n):
    temp = int(input())
    li.append(temp)

li = sorted(li)

for i in range(k):
    li.pop(0)
    li.pop(len(li)-1)

print(round(mean(li)))