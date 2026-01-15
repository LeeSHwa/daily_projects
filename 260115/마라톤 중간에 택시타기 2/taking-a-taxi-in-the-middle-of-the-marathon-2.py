n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# x = [p[0] for p in points]
# y = [p[1] for p in points]

min_distance = float('inf')


for passing in range(1, n-1): # passing : 1, 2
    distance = 0
    last_x = points[0][0]
    last_y = points[0][1]

    for i in range(n - 1): # i : 0, 1, 2, 3
        if  i + 1 == passing:
            i += 1
            # print(f"지금 {i}({points[i]})에서 뛰어넘었음")
            continue

        distance += abs(last_x - points[i+1][0]) + abs(last_y - points[i+1][1])
        # print(f"계산 중, last_x = {last_x}, last_y = {last_y}, points[{i+1}][0] = {points[i+1][0]}, points[{i+1}][1] = {points[i+1][1]}")
        last_x = points[i+1][0]
        last_y = points[i+1][1]

    min_distance = min(min_distance, distance)
    # print(f"{i + 1}. min_distance = {min_distance}")

print(min_distance)