# https://www.acmicpc.net/problem/18111

# 문제 - 마인크래프트
import sys
from collections import Counter

input = sys.stdin.readline

# N : 세로, M : 가로, B : 인벤토리 내 블록의 개수
N, M, B = map(int, input().split())

# 높이가 저장 될 2차원 배열
# (변경) -> extend를 통해 1차원으로 바로 처리
ground = []

# for _ in range(N):
#     ground.append(list(map(int, input().split())))
# 각 요소별 빈도수 계산 저장 변수
# counter = Counter([item for row in ground for item in row])

for _ in range(N):
    ground.extend(map(int, input().split()))

counter = Counter(ground)

# 브루트포스를 위해 순회할 범위 지정을 위한 최소, 최대 값
min_value = min(counter.keys())
max_value = max(counter.keys())

# 최소값을 구하기 위해 큰 값으로 설정
min_time = float('inf')
min_height = float('inf')

for height in range(min_value, max_value + 1):
    new_B = B
    time = 0
    
    # key 들의 값만 순회하여 각 요소에 개수만큼 곱해줌
    for key, frequency in counter.items():
        # key값과 height값의 차이값인 diff는 +/- 에 따라 분기 처리
        diff = key - height

        if key > height:  
            time += diff * 2 * frequency
            new_B += diff * frequency
        

        else:
            # diff가 마이너스이므로 -= 연산 (이하 동일)
            time -= diff * frequency
            new_B += diff * frequency
        
    # 만약 위 연산이 끝난 후 new_B가 마이너스라면 해당 연산은 모두 취소처리
    # (= 인벤토리의 B의 개수가 부족하다는 의미이기 때문)
    if new_B < 0:
        continue

    # 같은 값이라도 높이가 더 큰 쪽을 사용
    if time < min_time or (time == min_time and height > min_height):
        min_height = height
        min_time = time

print(min_time, min_height)