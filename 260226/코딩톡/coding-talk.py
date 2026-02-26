N, M, p = map(int, input().split())
timeline = {}

programmers = [chr(x) for x in range(65, 65 + N)]

for time in range(M):
    timeline[time] = input().split()

    if time >= (p - 1) and timeline[time][0] in programmers:
        programmers.remove(timeline[time][0])
        
if timeline[p - 1][1] == '0':
    exit()

print(*programmers)