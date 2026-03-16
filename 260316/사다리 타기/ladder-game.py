from collections import defaultdict

n, m = map(int, input().split())
height_dict = defaultdict(list)

ladders = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[(0, 1) for _ in range(n)] for _ in range(16)]

grid[0][1][2] += 1
grid[0][1]


