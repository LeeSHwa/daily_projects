# https://www.acmicpc.net/problem/2 869
import math

A, B, V = map(int,input().split())


temp = math.ceil(((V-A)/(A-B)))
if temp < 1:
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
