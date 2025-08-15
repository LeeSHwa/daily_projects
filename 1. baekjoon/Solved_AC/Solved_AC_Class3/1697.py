# https://www.acmicpc.net/problem/1697

# 문제 - 숨바꼭질
from collections import deque

N, K = map(int, input().split())

# N <= 100,000 / K <= 100,000
MAX_position = 100000

# start = N, target = K
def bfs(start, target):

    # 엣지케이스 / 만약 두 값이 같다면 움직일 필요 없이 바로 0 반환
    if start == target:
        return 0
    
    # 시작점으로 주어진 start와 이동횟수인 tries
    queue = deque([(start, 0)])

    # 1차원일 경우는 bool 형식이 좋음
    visited = [False] * (MAX_position + 1)
    visited[start] = True

    while queue:
        current, tries = queue.popleft()
        
        # 굳이 defaultdict로 저장하지 말고, 바로 next에 접근
        for next in [current - 1, current + 1, current * 2]:

            # next 값이 target와 같다면 tries + 1 출력
            if next == target:
                return tries + 1
            
            # 다르다면 값 범위 제한줌으로써 메모리 절약
            # 그리고 visited 여부 확인 후 enque 및 visited처리
            if  0 <= next <= MAX_position and not visited[next]:
                queue.append((next, tries + 1))
                visited[next] = True

print(bfs(N, K))