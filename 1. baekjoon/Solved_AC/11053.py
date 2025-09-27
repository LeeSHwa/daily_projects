# https://www.acmicpc.net/problem/11053

# 문제 - 가장 긴 증가하는 부분 수열
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

num_list = defaultdict(int)
max_num_list = -1

for i in range(N):
    if (N - i) < max_num_list:
        pass

    
    
    
    