# https://www.acmicpc.net/problem/18870

# 문제 - 좌표 압축

N = int(input())

array = list(map(int, input().split()))

set_array = set(array)
sorted_dict = {}
answer = []

for a, b in enumerate(sorted(set_array)):
    sorted_dict[b] = a

for num in array:
    answer.append(str(sorted_dict[num]))

print(' '.join(answer))