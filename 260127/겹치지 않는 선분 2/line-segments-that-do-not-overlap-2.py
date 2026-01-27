n = int(input())

pos = []

is_dup = [False] * n

for _ in range(n):
    pos.append(tuple(map(int, input().split())))

for i in range(n):
    x1, x2 = pos[i]

    for j in range(n):

        if j == i:
            continue

        diff_x1, diff_x2 = pos[j]

        if x1 > diff_x1 and x2 < diff_x2:
            is_dup[i] = True
            is_dup[j] = True

print(is_dup.count(False))

        