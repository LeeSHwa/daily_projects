X, Y = map(int, input().split())

# Please write your code here.

cnt = 0
for num in range(X, Y + 1):
    if len(set(list(map(int, str(num))))) == 2:
        cnt += 1

print(cnt)