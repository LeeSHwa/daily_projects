n = int(input())
grid = []
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
    # 탐색이 모두 끝났을 때
    if idx == len(exist):
        return
    
    row, col = pos
        
    # 종료조건
    if len(visited) == 3:
        ans = min(ans, move_count + abs(row - position['end'][0]) + abs(col - position['end'][1]))
        return

    visited.append(exist[idx])
    backtrack(position[exist[idx]], idx + 1, move_count + abs(row - position[exist[idx]][0]) + abs(col - position[exist[idx]][1]))

backtrack(position['start'], 0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)