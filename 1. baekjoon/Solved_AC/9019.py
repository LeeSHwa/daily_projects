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
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

for _ in range(T):

    A, B = map(int, input().split())
    
    answer = 0
    visited = [False] * 10000
    queue = deque([(A, '')])

    visited[A] = True

    while queue:
        x, comm = queue.popleft()
        
        if x == B:
            answer = comm
            break

        D_x = D(x)
        if not visited[D_x]:
            queue.append((D_x, comm + 'D'))
            visited[D_x] = True
        
        S_x = S(x)
        if not visited[S_x]:
            queue.append((S_x, comm + 'S'))
            visited[S_x] = True

        L_x = L(x)
        if not visited[L_x]:
            queue.append((L_x, comm + 'L'))
            visited[L_x] = True

        R_x = R(x)
        if not visited[R_x]:
            queue.append((R_x, comm + 'R'))
            visited[R_x] = True


    print(answer)