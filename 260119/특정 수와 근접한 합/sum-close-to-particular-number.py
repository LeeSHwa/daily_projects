N, S = map(int, input().split())

nums = list(map(int, input().split()))


all_sum = sum(nums)
mins = float('inf')

for i in range(N-1):
    for j in range(i+1, N):
        temp = all_sum
        
        aaa = temp - nums[i] - nums[j]

        mins = min(mins, aaa)

print(mins - S)
            