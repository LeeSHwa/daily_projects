# https://www.acmicpc.net/problem/1931

# 문제 - 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())

meeting = []

for _ in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])
    
sorted_meeting = sorted(meeting)

temp = {}

for i, j in sorted_meeting:
    
    if temp[i]:
        temp[i] = min(temp[i], j)
        continue
    
    temp[i] = j

print(temp)

# 일단 새롭게 들어오는 meeting의 start가 기존에 있던 meeting의 end보다 크다면 추가?
# cur_start > next_start and cur_end > next_end ??

# 정렬을 어떻게 하지??
# start 순으로 정렬을 해야하나?? 아니면 범위별로??

