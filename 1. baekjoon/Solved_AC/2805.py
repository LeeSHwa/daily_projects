# https://www.acmicpc.net/problem/2805

# 문제 - 나무 자르기

N, M = map(int, input().split())

trees = list(map(int, input().split()))

end = max(trees)
start = 0
answer = 0

while start <= end:
    count = 0
    mid = (end + start) // 2

    for i in range(N):
        if trees[i] > mid:
            count += (trees[i] - mid)

    if M >= count:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1


print(answer)