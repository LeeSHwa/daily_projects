from collections import defaultdict

n, m = map(int, input().split())
height_dict = defaultdict(list)

ladders = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0 for _ in range(n)] for _ in range(16)]

def apply_grid(row, col, val): # val 1 : apply / va2 -1 : return
    
    if val == 1:
        grid[row][col] = 1

    else:
        grid[row][col] = 0
        
def play_game():
    pos = list(range(1, n + 1))

    for depth in range(16):
        line = grid[depth]
        
        for idx in range(n - 1):
            if line[idx]:
                pos[idx], pos[idx + 1] = pos[idx + 1], pos[idx]
    
    return pos

for i in range(m):
    c, r = ladders[i]

    apply_grid(r - 1, c - 1, 1)

answer_pos = play_game()
min_cnt = m

def recurr(depth, cnt):
    global min_cnt

    # 0. 종료조건
    if depth == m:
        curr_pos = play_game()

        if curr_pos == answer_pos:
            min_cnt = min(min_cnt, cnt)

        return

    c, r = ladders[depth]
    
    # 1. 제거
    apply_grid(r - 1, c - 1, -1)

    # 2. 제거한 상태에서 탐색
    recurr(depth + 1, cnt - 1)

    # 3. 복구
    apply_grid(r - 1, c - 1, 1)

    # 4. 제거하지 않은 상태에서 탐색
    recurr(depth + 1, cnt)

recurr(0, min_cnt)

print(min_cnt)