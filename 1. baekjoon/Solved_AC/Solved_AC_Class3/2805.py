# https://www.acmicpc.net/problem/2805

# 문제 - 나무 자르기

N, M = map(int, input().split())

trees = list(map(int, input().split()))

end = max(trees)
start = 0
answer = 0

# 이분탐색 구현
while start <= end: 
    count = 0
    mid = (end + start) // 2

    # mid보다 큰 나무들만 잘라서 얻을 수 있는 나무 길이를 계산
    for i in range(N):
        if trees[i] > mid:
            count += (trees[i] - mid)

    # 잘린 나무 길이 합이 M 이상이면, 톱 높이를 더 올려서 최대값 탐색
    if count >= M:
        answer = mid    # 현재 mid가 정답을 충족하니 우선 정답처리
        start = mid + 1 # 더 높은 높이를 시도
    else:
        end = mid - 1   # 잘린 양 부족, 높이를 낮춰서 더 많이 자르기

print(answer)