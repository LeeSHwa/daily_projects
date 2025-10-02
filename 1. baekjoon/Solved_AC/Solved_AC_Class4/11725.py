# https://www.acmicpc.net/problem/11725

# 문제 - 트리의 부모 찾기

from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
parent = {}

def DFS(start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            parent[node] = start
            DFS(node)
            
DFS(1)

sorted_parent = dict(sorted(parent.items()))

for i in sorted_parent.values():
    print(i)