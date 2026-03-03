n, m = map(int, input().split())
arr = list(map(int, input().split()))

def count_one(arr, m):
    
    window = arr[: m + 1]
    count_array = []

    for i in range(len(arr)):
        window = arr[max(0, i - m): min(i + m + 1, len(arr))]
        count_array.append(window.count(1))
    
    return count_array

cnt = 0
array = count_one(arr, m)

while True:
    if max(array) == 0:
        break

    highest = max(array)

    highest_idx = array.index(highest)

    for i in range(max(0, highest_idx - m), min(highest_idx + m + 1, len(arr))):
        arr[i] = 0

    cnt += 1  
    
    array = count_one(arr, m)

print(cnt)