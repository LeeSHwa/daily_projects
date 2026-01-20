N, K = map(int, input().split())
position = [0] * 10001

max_pos = -1
for _ in range(N):
    pos, alaph = input().split()
    pos = int(pos)
    if alaph == 'G':
        alaph = 1
    else:
        alaph = 2

    position[pos] = alaph
    max_pos = max(max_pos, pos)

first_sum = sum(position[1 : K])

sum_of_nums = [first_sum]
for i in range(1, max_pos - K + 1):
    sum_of_nums.append(first_sum - position[i] + position[i + K])

print(max(sum_of_nums))
