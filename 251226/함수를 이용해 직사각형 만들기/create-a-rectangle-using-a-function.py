def print_ones(row, col):
    line = "*" * row
    for _ in range(col):
        print(line)

row, col = map(int, input().split())