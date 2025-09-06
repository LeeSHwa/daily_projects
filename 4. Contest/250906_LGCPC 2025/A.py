from collections import deque
import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    # N : 서브태스크의 개수 / M : 위계의 수
    N, M = map(int, input().split())
    
    # 각 서브태스크의 배점
    score = deque(map(int, input().split()))
    score.appendleft(0)
    
    print(score)

    # 아니 그냥 애초에 나올 수 있는 점수의 경우의 수를 모두 구해두는게 맞지 않을까?
    # 근데 그걸 어떻게 구함??
    # 0점부터 각 요소의 덧셈들이 필요한디
    # 근데? 경우의 수를 구하는 거임

    hierarchy = [0] * (100 * P)
    # 위계
    for _ in range(M):
        must_solve, to_solve = map(int, input().split())
        hierarchy[to_solve] = must_solve
