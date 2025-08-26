# https://www.acmicpc.net/problem/1931

# 문제 - 회의실 배정
import sys

input = sys.stdin.readline

N = int(input())

meeting = []

for _ in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])
    
sorted_meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

pre_end = 0
count = 0

for start, end in sorted_meeting:
    if start >= pre_end or (start == pre_end and start == end):
        pre_end = end
        count += 1

print(count)