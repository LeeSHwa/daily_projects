N = int(input())

nums = list(map(int, input().split()))

nums.sort()

cnt = 0
for K in range(1, 101):
    for num in nums:
        if K > num:
            diff = K - num

            if K + diff in nums:
                cnt += 1   

print(cnt)