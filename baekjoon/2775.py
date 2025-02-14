# https://www.acmicpc.net/problem/2775

T = int(input())

while T > 0:
    k = int(input())
    n = int(input())

    matrix = []
    temp = []

    for i in range(k):
        
        for j in range(1,n+1):
            temp.append(j)

        matrix.append(temp)
        print(matrix)
