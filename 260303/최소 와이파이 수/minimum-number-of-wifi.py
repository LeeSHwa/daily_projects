n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
curr = 0
while curr < n - 1:
    if arr[curr] == 1:
        curr += 2 * m + 1
        cnt += 1
    
print(cnt)