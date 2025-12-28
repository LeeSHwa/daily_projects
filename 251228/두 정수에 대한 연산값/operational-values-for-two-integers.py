def calculate_magic_num(a, b):
    min_num = min(a, b)
    max_num = max(a, b)

    return min_num * 2, max_num + 25

a, b = map(int, input().split())
a, b = calculate_magic_num(a, b)
print(a, b)
