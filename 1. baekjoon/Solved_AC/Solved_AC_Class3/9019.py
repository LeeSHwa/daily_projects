# https://www.acmicpc.net/problem/9019

# 문제 - DSLR
from collections import deque
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
    
    visited = [False] * 10000
    queue = deque([(A)])
    parent = [0] * 10000
    how = [''] * 10000

    visited[A] = True

    while queue:
        current= queue.popleft()
        
        if current == B:
            break 

        next_node = D(current)
        if not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True
            parent[next_node] = current
            how[next_node] = 'D'
        
        next_node = S(current)
        if not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True
            parent[next_node] = current
            how[next_node] = 'S'

        next_node = L(current)
        if not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True
            parent[next_node] = current
            how[next_node] = 'L'

        next_node = R(current)
        if not visited[next_node]:
            queue.append(next_node)
            visited[next_node] = True
            parent[next_node] = current
            how[next_node] = 'R'

    curr = B
    answer = ''

    while curr != A:
        answer += how[curr]
        curr = parent[curr]

    print(answer[::-1])