N, K = map(int, input().split())

positions = [0] * 101
max_pos = -1
min_pos = 101

for _ in range(N):
    candy, pos = map(int, input().split())
    
    positions[pos] = candy
    max_pos = max(max_pos, pos)
    min_pos = min(min_pos, pos)

search_range = 2 * K + 1

max_candy = -1
window = []
ans = 0

for pos in range(min_pos, max_pos - search_range + 1):
    window = positions[pos : pos + search_range]

    sum_window = sum(window)
    if sum_window > max_candy:
        max_candy = max(max_candy, sum_window)

print(max_candy)