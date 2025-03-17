N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

B_start = [[ 'B' if (i+j)%2 ==0 else 'W' for j in range(8)] for i in range(8)]
W_start = [[ 'W' if (i+j)%2 ==0 else 'B' for j in range(8)] for i in range(8)]

min_cnt = float('inf')

for i in range(N-7):  # 수정된 반복문 범위
    for j in range(M-7):
        cnt_b = 0
        cnt_w = 0
        for a in range(8):  # a: 패턴 행 인덱스
            for b in range(8):  # b: 패턴 열 인덱스
                current = matrix[i+a][j+b]
                if current != B_start[a][b]:
                    cnt_b += 1
                if current != W_start[a][b]:
                    cnt_w += 1
        min_cnt = min(min_cnt, cnt_b, cnt_w)

print(min_cnt)
