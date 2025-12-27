def is_contain(A, B):
    A = ''.join(map(str, A))
    B = ''.join(map(str, B))

    if B in A:
        print("Yes")
        return

    else:
        print("No")
        return
    
len_A, len_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_contain(A, B)
