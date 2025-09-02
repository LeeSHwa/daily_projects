# https://www.acmicpc.net/problem/9019

# 문제 - DSLR
from collections import defaultdict, deque
import sys

input = sys.stdin.readline

T = int(input())

def D(n):
    if n * 2 > 9999:
        return n * 2 % 10000

    else:
        return n * 2

def S(n):
    if n == 0:
        return 9999
    
    else:
        return n - 1

def L(n):
    list_n = deque(list(str(n)))
    temp = list_n.popleft()
    list_n.append(temp)
    n = int(''.join(list_n))
    return n

def R(n):
    list_n = deque(list(str(n)))
    temp = list_n.pop()
    list_n.appendleft(temp)
    n = int(''.join(list_n))
    return n

print(L(1000))
print(R(1000))

    
# for _ in range(T):
#     A, B = map(int, input().split())
    
#     queue = deque([(A, [])])

#     dictionary = defaultdict(list)
#     dictionary[A] = 

#     while queue:
#         x, comm = queue.popleft()
        
#         for A in dictionary[x]:

