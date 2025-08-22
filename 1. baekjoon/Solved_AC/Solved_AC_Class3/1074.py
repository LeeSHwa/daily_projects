# https://www.acmicpc.net/problem/1074

# 문제 - Z

N, r, c = map(int, input().split())

length = width = 2**N

order = 0

size = 2 ** N
# matrix = [[x] * length for x in range(width)]

# index = 0

# square_1 = [matrix[x][: length//2] for x in range(width // 2)] # 왼쪽 위
# square_2 = [matrix[x][length//2 : length] for x in range(width // 2)] # 오른쪽 위
# square_3 = [matrix[x][: length//2] for x in range(width // 2, width)] # 왼쪽 아래
# square_4 = [matrix[x][length//2 : length] for x in range(width // 2, width)] # 오른쪽 아래

def Z(row, col, size, order):
    if size == 1:
        return order

    dsize = size // 2

    if 0 <= row < size//2 and 0 <= col < size//2: # 왼쪽 위
        return Z(row, col, size//2, order)
    
    elif 0 <= row < size//2 and size//2 <= col < size: # 오른쪽 위
        order += size*size//4
        return Z(row, col - dsize, size//2, order)
    
    elif size//2 <= row < size and 0 <= col < size//2: # 왼쪽 아래
        order += 2 * size*size//4
        return Z(row - dsize, col, size//2, order)

    else: # 그 외
        order += 3 * size*size//4
        return Z(row - dsize, col - dsize, size//2, order)
    

print(Z(r, c, size, order))