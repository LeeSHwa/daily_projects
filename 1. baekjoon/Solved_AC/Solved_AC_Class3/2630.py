# https://www.acmicpc.net/problem/2630

# 문제 - 색종이 만들기

n = int(input())
matrix1 = []
for i in range(n):
    matrix1.append(list(map(int,input().split())))

white = 0
blue = 0

def count_color(x, y, size):
    global white, blue
    color = matrix1[x][y] # 시작점의 색

    all_same = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix1[i][j] != color:
                all_same = False
                break
        if not all_same: # 이미 순회중인 경우도 제외
            break
        
    if all_same: # 사각형 속 숫자가 모두 같다면
        if color == 0: # white
            white += 1
        else:          # blue
            blue += 1
        return
    
    half = size // 2
    count_color(x, y, half)    # 왼쪽 위
    count_color(x + half, y, half)    # 오른쪽 위
    count_color(x, y + half, half)    # 왼쪽 아래
    count_color(x + half, y + half, half)    # 오른쪽 아래

count_color(0, 0, n)
print(white)
print(blue)
    
