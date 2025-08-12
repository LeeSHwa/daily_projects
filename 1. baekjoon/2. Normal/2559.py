# https://www.acmicpc.net/problem/2559

# 문제 - 수열

N, K = map(int, input().split())
temp = list(map(int, input().split()))

left = 0
right = K
max_value = current = sum(temp[left:right])


while right < N:
    next = current - temp[left] + temp[right]
    max_value = max(max_value, next)

    current = next
    left += 1
    right += 1

print(max_value)