# https://www.acmicpc.net/problem/1676

import math

N = int(input())
flag = False
cnt = 0

li = list(map(int,str(math.factorial(N))))

while flag == False: 
    if li[-1] == 0:
        cnt += 1
        li.pop(-1)
        
    else:
        flag = True

print(cnt)

