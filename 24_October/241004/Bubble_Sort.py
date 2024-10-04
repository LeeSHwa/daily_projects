def Bubble_Sort(arr): # O(n^2)
    n = len(arr) # 배열의 길이
    
    for end in range(n-1, 0, -1): # 배열의 끝 end
        for cur in range(0,end): # 현재 위치 cur
            if arr[cur] > arr[cur+1]: # 현재 값이 다음 값보다 크면
                arr[cur],arr[cur+1] = arr[cur+1],arr[cur] # 큰 수를 뒤로 보낸다.
    
    return arr

arr = [5, 4, 3, 2, 1]
A = Bubble_Sort(arr)
print(A)