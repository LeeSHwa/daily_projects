# https://www.acmicpc.net/problem/11724

# 문제 - 연결 요소의 개수
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

graph = defaultdict(list)
input = sys.stdin.readline

# N : 정점의 개수 / M : 간선의 개수
N, M = map(int, input().split())

# visited는 bool 형식으로 관리 (list로 저장 후 in 연산시 O(n), 하지만 bool은 O(1))
visited = [False] * (N + 1)
count = 0

# u : 시작점, v: 도착점
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, start):
    
    visited[start] = True
    
    for x in graph[start]: # graph[start]의 values 순회
        if not visited[x]: # 만약 해당 노드를 순회하지 않았다면
            dfs(graph, x)  # 재귀 순회


# for x in graph.keys():  # 해당 방법은 모든 정점을 순회하지 못 할 수도 있음
for x in range(1, N + 1): # 모든 정점을 순회하기 위해 1 ~ N까지 순회
    if not visited[x]:  # 만약 방문하지 않은 노드라면
        count += 1      # 새로운 연결요소이기 때문에 집계 += 1
        dfs(graph, x)
    
print(count)