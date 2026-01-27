h, w = map(int, input().split())
blocks = list(map(int, input().split()))

LEFT = [0] * w
RIGHT = [0] * w

temp = 0
for i in range(w):
    LEFT[i] = temp
    temp = max(temp, blocks[i])

temp = 0
for i in range(w-1, -1, -1):
    RIGHT[i] = temp
    temp = max(temp, blocks[i])

answer = 0
for i in range(w):
    if blocks[i] < LEFT[i] and blocks[i] < RIGHT[i]:
        rain = min(LEFT[i], RIGHT[i]) - blocks[i]
        answer += rain

print(answer)