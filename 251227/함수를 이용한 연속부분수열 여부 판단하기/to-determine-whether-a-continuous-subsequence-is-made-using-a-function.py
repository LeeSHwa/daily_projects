def is_contain(A, B):
    if B[0] in A:
        start = A.index(B[0])
        flag = False
        for curr in range(start, len(A) + 1 - len(B)):
            for j in range(0, len(B)):
                if A[curr + j] == B[j]:
                    pass
                else:
                    flag = True
            if flag:
                continue
            else:
                print("Yes")
                return
        print("No")
        return
    else:
        print("No")
        return
    
    
    
len_A, len_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

is_contain(A, B)
