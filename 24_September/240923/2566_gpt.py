M, N = 9, 9
arr = []

for i in range(M):
    # 한 줄의 입력을 받아 정수 리스트로 변환한 후 arr에 추가
    temp = list(map(int, input().split()))
    arr.append(temp)

# 2차원 배열에서 최댓값을 찾음
max_value = -1
max_pos = (0, 0)

for i in range(M):
    for j in range(N):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_pos = (i + 1, j + 1)  # 좌표는 1부터 시작하기 때문에 1을 더함

print(max_value)
print(max_pos[0], max_pos[1])