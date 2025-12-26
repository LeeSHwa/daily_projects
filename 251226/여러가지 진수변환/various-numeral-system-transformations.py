N, B = map(int, input().split())

# Please write your code here.

num = 0

for bit in N:
    num = num * B + bit

print(num)