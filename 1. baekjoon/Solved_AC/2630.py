# https://www.acmicpc.net/problem/2630

# 문제 - 색종이 만들기

# N은 최대 128임, 그럼 그냥 하나하나 다 순회한다고 생각해도 괜찮을 듯
# 모두 순회하다 0이 나오면 break 후 쪼개기? 
# 슬라이싱으로 쪼개볼까?

N = int(input())
flag = False

lines = []
for i in range(N):
    lines.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if lines[i][j] == 0:
            flag = True
            break

array = []

# for a in range(N):
#     for b in range(N):
#         print(lines[a][b], end =" ")
#     print()

# 슬라이싱을 어떻게 하지?
# 일단 기본적으로 다 순회하고
# 아니면 다 