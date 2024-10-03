N, M = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()
max_sum = 0

# 첫 번째 카드를 고정하고, 나머지 두 개를 투 포인터로 탐색
for i in range(N - 2):
    left, right = i + 1, N - 1
    while left < right:
        current_sum = cards[i] + cards[left] + cards[right]
        
        if current_sum <= M:
            max_sum = max(max_sum, current_sum)
            left += 1  # 합이 M보다 작으면 더 큰 합을 찾아야 하므로 왼쪽 포인터를 증가
        else:
            right -= 1  # 합이 M보다 크면 더 작은 합을 찾아야 하므로 오른쪽 포인터를 감소

print(max_sum)