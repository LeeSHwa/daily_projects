N = int(input())

nums = list(map(int, input().split()))

count = 0

for i in range(N-1): # 0
    for j in range(i+1, N): # 1
        window = []

        for num in range(i, j):
            window.append(nums[num])

        if sum(window) // (j-i) in window: # nums[0] // 1
            count += 1

print(count)