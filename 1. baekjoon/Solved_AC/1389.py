# https://www.acmicpc.net/problem/1389
import sys
from collections import defaultdict

input = sys.stdin.readline

friends = defaultdict(set)

N, M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

# dfs를 사용해야함, visited는 그때그때 초기화
# 스택? 재귀?
# 기준 점에서 각 점까지 도달하는데 걸리는 횟수의 총합..
# 횟수가 같다면 번호가 가장 작은 친구

