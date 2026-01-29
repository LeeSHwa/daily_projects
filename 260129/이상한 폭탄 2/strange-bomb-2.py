N, K = map(int, input().split())

booms = [int(input()) for _ in range(N)]
is_booms = [False] * N

for i in range(N - 1):
    if i + 1 + K < N:
        for j in range(i + 1, i + 1 + K):
            if booms[i] == booms[j]:
                is_booms[j] = True

for i in range(N-1, -1, -1):
    if is_booms[i] == True:
        print(i)
        break