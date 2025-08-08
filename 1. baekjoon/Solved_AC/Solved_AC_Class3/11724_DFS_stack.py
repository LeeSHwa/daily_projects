# https://www.acmicpc.net/problem/11724

# 문제 - 연결 요소의 개수
import sys
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

# DFS를 stack로 구현
stack = []

# 모든 정점을 순회
for x in range(1, N + 1): 

    if not visited[x]: 
        count += 1

        # 스택을 이용한 DFS 시작
        stack = [x]
        visited[x] = True # pop 하기 전에 방문처리 / 이해가 잘 되진 않음, 이해되면 주석 수정예정

    # stack에 값이 있을 경우에만 실행(= visited되지 않은 노드를 찾았을 때에만 실행)
    while stack:
        popped = stack.pop()   # 순회 할 노드를 정함
        
        for neighbor in graph[popped]:   # 순회할 노드의 주변 노드들 탐색
            if not visited[neighbor]:    # 만약 not visited 라면
                visited[neighbor] = True # visited 처리 후
                stack.append(neighbor)   # 해당 노드를 기준으로 또다시 탐색



print(count)