# https://www.acmicpc.net/problem/1074

# 문제 - Z

N, r, c = map(int, input().split())

matrix = [[-1] * N for _ in range(N)]

index = 0
def Z(start_row, start_col):

    
    matrix[start_row][start_col] = index
    matrix[start_row][start_col + 1] = index + 1
    matrix[start_row + 1][start_col] = index + 2 
    matrix[start_row + 1][start_col + 1] = index + 3

    index += 4

    if start_col + 1 == 2**N - 1:
        
        


    

    