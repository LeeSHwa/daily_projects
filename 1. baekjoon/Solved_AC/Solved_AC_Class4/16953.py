# https://www.acmicpc.net/problem/16953

# 문제 - A → B

# 1. 2를 곱한다 / 2. 1을 수의 가장 오른쪽에 추가한다.

# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력, 만들 수 없는 경우 -1 출력

A, B = map(int, input().split())

nums = {}

def gob(num, depth):
    num_1 = num * 2
    num_2 = num * 10 + 1

    if num_1 <= B:
        if num_1 == B:
            print(depth + 1)
            exit()
        nums[num_1] = depth
        gob(num_1, depth + 1)

    if num_2 <= B:
        if num_2 == B:
            print(depth + 1)
            exit()
        nums[num_2] = depth
        gob(num_2, depth + 1)

gob(A, 1)
print(-1)