N, B = map(int, input().split())

# Please write your code here.

digits = []

while True:
    if N < 4:
        digits.append(N)
        break
    
    digits.append(N % B)

    N //= B

digits = digits[::-1]
print(''.join(map(str, digits)))