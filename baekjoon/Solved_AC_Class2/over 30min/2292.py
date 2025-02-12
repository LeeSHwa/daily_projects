# https://www.acmicpc.net/problem/2292

N = int(input())
temp = 1
while True:
    if N == 1:
        break

    N -= (temp-1)*6
    if N > 1:
        temp += 1
    else:
        break

print(temp)