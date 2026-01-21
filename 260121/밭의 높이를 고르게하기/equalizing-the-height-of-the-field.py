N, H, T = map(int, input().split()) # N개의 밭, H의 높이를 만족하는 밭이 최소 T개가 되도록

field = list(map(int, input().split()))
diff = []

for idx in range(N):
    if field[idx] == H:
        T -= 1
    diff.append(abs(field[idx] - H))
            
diff.sort(reverse=True)

ans = 0
for i in range(len(diff) - 1, -1, -1):
    if diff[i] == 0:
        continue
    else:
        ans += diff[i]
        T -= 1
        if T == 0:
            break

print(ans)