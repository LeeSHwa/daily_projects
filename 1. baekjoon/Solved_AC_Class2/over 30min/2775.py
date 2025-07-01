# https://www.acmicpc.net/problem/2775

T = int(input())

while T > 0:
    k = int(input())
    n = int(input())

    matrix = []
    temp1 = []

    for i in range(1,n+1):
        temp1.append(i)

    matrix.append(temp1)

    for j in range(1,k+1):
        tmp = []
        for p in range(1,n+1):
            tmp.append(sum(matrix[j-1][:p]))
            
        matrix.append(tmp)

    print(matrix[k][n-1])
    
    T -= 1
