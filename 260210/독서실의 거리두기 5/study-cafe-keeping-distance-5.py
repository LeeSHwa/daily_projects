N = int(input())
seats = input()

MAX_DISTANCE = 20

distance = [MAX_DISTANCE] * N 

cnt = MAX_DISTANCE
# LEFT
for i in range(N):

    if seats[i] == '1':
        cnt = 0
    else:
        cnt += 1

    distance[i] = cnt

print(*distance)

cnt = MAX_DISTANCE
# RIGHT
for i in range(N - 1, -1, -1):

    if seats[i] == '1':
        cnt = 0
    else:
        cnt += 1

    distance[i] = min(distance[i], cnt)

print(max(distance))