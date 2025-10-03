# https://www.acmicpc.net/problem/15663

# 문제 - N과 M (9)

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

line = []
# nums의 '인덱스'를 방문했는지 여부를 체크합니다.
visited_index = [False] * N

def backtrack():
    # 수열이 완성되면 출력합니다.
    if len(line) == M:
        print(' '.join(map(str, line)))
        return

    last_num = 0
    
    # 0부터 N-1까지 '인덱스'를 기준으로 순회합니다.
    for i in range(N):
        # 이미 방문한 인덱스거나, 같은 레벨에서 이미 사용한 숫자이면 건너뜁니다.
        if visited_index[i] or last_num == nums[i]:
            continue

        # 1. 상태 변경 : i번째 인덱스를 방문했다고 표시합니다.
        visited_index[i] = True
        line.append(nums[i])
        last_num = nums[i]
        
        # 2. 재귀 호출 : 다음 숫자를 찾으러 떠납니다.
        backtrack()
        
        # 3. 상태 원상복구 : 재귀가 끝나고 돌아오면 다른 경로의 탐색을 위해 방금 변경했던 상태를 원래대로 되돌립니다.
        visited_index[i] = False
        line.pop()

backtrack()