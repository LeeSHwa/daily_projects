n = int(input())
position = {}
exist = []

for row in range(n):
    line = list(input())

    for col in range(n):
        if line[col] == 'S':
            position['start'] = (row, col)
        elif line[col] == 'E':
            position['end'] = (row, col)
        elif line[col] != '.':
            position[int(line[col])] = (row, col)
            exist.append(int(line[col]))

exist.sort()

visited = []
ans = float('inf')

def backtrack(pos, idx, move_count):
    global ans
    
    row, col = pos

    # 가지치기
    if move_count >= ans:
        return
    # 종료조건
    if len(visited) == 3:
        distance = move_count + abs(row - position['end'][0]) + abs(col - position['end'][1])
        if ans > distance:
            ans = distance
        return
    
    # 탐색이 모두 끝났을 때
    if idx == len(exist):
        return

    visited.append(exist[idx])
    backtrack(position[exist[idx]], idx + 1, move_count + abs(row - position[exist[idx]][0]) + abs(col - position[exist[idx]][1]))
    visited.pop()

    backtrack(pos, idx + 1, move_count)

backtrack(position['start'], 0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)