n = int(input())
arr = list(map(int, input().split()))

def cal(n):
    if 2 in arr and arr[n] > 2:
        if arr[n] % 2 == 0:
            arr[n] //= 2

    if 3 in arr and arr[n] > 3:
        if arr[n] % 3 == 0:
            arr[n] //= 3

    if 5 in arr and arr[n] > 5:            
        if arr[n] % 5 == 0:
            arr[n] //= 5

    if n == 0:
        return arr[0]

    return cal(n - 1) * arr[n]



print(cal(n-1))
    