N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]


for bar1_row in range(N):
    for bar1_col in range(N-2):
        bar1 = grid[bar1_row][bar1_col] + grid[bar1_row][bar1_col + 1] + grid[bar1_row][bar1_col + 2]
        
        prnit(bar1)
        

