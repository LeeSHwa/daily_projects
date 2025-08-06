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

array = []

size = N

def divide(lines, size):
    temp1 = [lines[: size//2] for _ in range(lines[:size//2])]
    return temp1

ans = divide(lines, size)
print(ans)
