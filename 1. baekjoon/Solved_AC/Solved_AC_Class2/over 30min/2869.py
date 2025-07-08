# https://www.acmicpc.net/problem/2869
import math

A, B, V = map(int,input().split())

if A == V:
    print(1)
else:
    temp = math.ceil(((V-A)/(A-B)))
    if V < 2*A - B:
        temp = 1

    print(math.floor(temp + 1))

# while height < V:
#     cnt += 1
#     height += A
    
#     if height >= V: 
#         break
#     else:
#         height -= B
#         continue
