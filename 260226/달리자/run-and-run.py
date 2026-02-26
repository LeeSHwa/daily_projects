n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [a - b for a, b in zip(A, B)]

length = 0
for i in range(n - 1):
    if diff[i] > 0:
        length += diff[i]
        diff[i+1] += diff[i]
    else:
        diff[i] += diff[i-1]
        length += diff[i]

print(length)