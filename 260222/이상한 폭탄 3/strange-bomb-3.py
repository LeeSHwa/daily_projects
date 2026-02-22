from collections import defaultdict

n, k = map(int, input().split())
booms = defaultdict(list)

def is_closed(array):
    length = len(array)
    explosion = 0
    last_num = array[0]

    for idx in range(1, length):
        if array[idx] - last_num <= k:
            explosion += 1
        last_num = array[idx]

    return explosion

for idx in range(n):
    boom = int(input())

    booms[boom].append(idx)
    
for elem in booms:
    booms[elem] = is_closed(booms[elem])

ans = sorted(booms.items(), key = lambda x : (-x[1], -x[0]))

print(ans[0][0])