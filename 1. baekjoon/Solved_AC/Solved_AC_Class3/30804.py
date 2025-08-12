# https://www.acmicpc.net/problem/30804

# 문제 - 과일 탕후루
from collections import defaultdict

N = int(input())
candies = input().split()

# 투 포인터 문제(슬라이딩 윈도우)
left = right = 0

# 값 별로 저장할 딕셔너리 (종류 집계에 도움을 줌)
counter = defaultdict(int)

counter[candies[0]] = 1
longest = 1 

# right 포인터가 N보다 작을 때 (= 아직 배열의 끝에 도달하지 못했을 때)
while right < N:

    # 종류가 2개 이하라면 right 포인터를 움직임
    if len(counter) <= 2:
        # 움직이기 전 최대길이를 항상 비교 및 저장
        longest = max(longest, right - left + 1)
        right += 1

        # 만약 right가 N이 되었다면 indexerror 발생, 이를 방지하기 위해 아래 조건 추가
        if right < N:
            counter[candies[right]] += 1

    # 종류가 3개 이상이라면 left 포인터를 움직임
    else:
        counter[candies[left]] -= 1
        if counter[candies[left]] == 0:
            del counter[candies[left]]
        left += 1 

print(longest)