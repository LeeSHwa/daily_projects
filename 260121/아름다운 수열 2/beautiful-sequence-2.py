import itertools

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

buti = list(itertools.permutations(B, M))

start = 0
end = M
count = 0

for _ in range(N - M + 1): # 8 - 3
    window = tuple(A[start:end])

    for num in buti:
        if window == num:
            count += 1

    start += 1
    end += 1

print(count)