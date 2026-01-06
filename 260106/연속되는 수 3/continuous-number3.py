N = int(input())

array = [int(input()) for _ in range(N)]
count = 0
max_count = -1

is_positive = False

for i in range(N):
    if i == 0:
        count = 1
        continue
    
    if array[i] * array[i-1] >= 0:
        count += 1
        max_count = max(max_count, count)
    
    else:
        count = 1
        
print(max_count)