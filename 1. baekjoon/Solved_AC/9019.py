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

# def L(n):
#     list_n = deque(list(str(n)))
#     temp = list_n.popleft()
#     list_n.append(temp)
#     n = int(''.join(list_n))
#     return n

# def R(n):
#     list_n = deque(list(str(n)))
#     temp = list_n.pop()
#     list_n.appendleft(temp)
#     n = int(''.join(list_n))
#     return n

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

for _ in range(T):

    A, B = map(int, input().split())
    
    answer = 0
    visited = set()
    queue = deque([(A, '')])

    visited.add(A)

    while queue:
        x, comm = queue.popleft()
        
        if x == B:
            answer = comm
            break

        D_x = D(x)
        if D_x not in visited:
            queue.append((D_x, 'D' + comm))
            visited.add(D_x)
        
        S_x = S(x)
        if S_x not in visited:
            queue.append((S_x, 'S' + comm))
            visited.add(S_x)

        L_x = L(x)
        if L_x not in visited:
            queue.append((L_x, 'L' + comm))
            visited.add(L_x)

        R_x = R(x)
        if R_x not in visited:
            queue.append((R_x, 'R' + comm))
            visited.add(R_x)


    print(answer)