# https://www.acmicpc.net/problem/1018

N, M = map(int, input().split()) # M * N의 배열임

matrix = []

for i in range(N): 
    temp = input()
    
    matrix.append(list(temp))

# B_start 생성, i + j가 짝수면 W 출력, 아니면 B 출력
B_start = [['B' if (i+j) % 2 == 0 else 'W' for j in range(8)] for i in range(8)]

# W_start 생성
W_start = [['W' if (i+j) % 2 == 0 else 'B' for j in range(8)] for i in range(8)]

# B_start = [
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B']
# ]

# W_start = [
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W'],
# ['W','B','W','B','W','B','W','B'],
# ['B','W','B','W','B','W','B','W']
# ]

cnt = 1000000

for i in range(N - 7):
    for j in range(M - 7):
        a = b = 0
        temp1 = temp2 = 0

        for p in range(i, i+8):
            b = 0
            for q in range(j, j+8):
                if matrix[p][q] != B_start[a][b]:
                    temp1+=1
                if matrix[p][q] != W_start[a][b]:
                    temp2+=1
                
                b += 1
            a += 1

        cnt = min(cnt, temp1, temp2)

print(cnt)

