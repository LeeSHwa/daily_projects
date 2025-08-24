# https://www.acmicpc.net/problem/1931

# 문제 - 회의실 배정
import sys
input = sys.stdin.readline

N = int(input())

meeting = []

for _ in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])
