SIZE = 10

grid = []
L = ()
R = ()
B = ()

for row in range(SIZE):
    line = list(input())
    grid.append(line)

    for idx in range(SIZE):
        if line[idx] == 'L':
            L = (row, idx)
        elif line[idx] == 'R':
            R = (row, idx)
        elif line[idx] == 'B':
            B = (row, idx)

distance = 0
if (L[0] == R[0] and R[0] == B[0]) or (L[1] == R[1] and R[1] == B[1]):
    if abs(L[0] - R[0]) < abs(L[0] - B[0]) or abs(L[1] - R[1]) < abs(L[1] - B[1]):
        distance = max(abs(B[0] - L[0]), abs(B[1] - L[1])) + 1
    else:
        distance = abs(B[0] - L[0]) +  abs(B[1] - L[1]) - 1
else:
    distance = abs(B[0] - L[0]) +  abs(B[1] - L[1]) - 1

print(distance)