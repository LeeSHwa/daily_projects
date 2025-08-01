# https://www.acmicpc.net/problem/34099

# 문제 - 뭔가 이미 있을 것 같은 순열 문제

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    
    array = [x for x in range(1, N+1)]

    if K == 1:
        if N == 2 or N == 3:
            print(-1)
        elif N == 4:
            print("2 4 1 3")
        elif N % 2 == 0:
            for i in range(1, N, 2):
                print(i, end=" ")
            for j in range(2, N+1, 2):
                print(j, end=" ")
            print()
        elif N % 2 == 1:
            for i in range(1, N+1, 2):
                print(i, end=" ")
            for j in range(2, N, 2):
                print(j, end=" ")
            
    else:
        print(' '.join(map(str, array)))
    print()
