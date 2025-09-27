# https://www.acmicpc.net/problem/11053

# 문제 - 가장 긴 증가하는 부분 수열

# 만약.. max_num이 current가 아니라면? 

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

num_list = defaultdict(int)
max_num_list = -1

for i in range(N):
    if (N - i) < max_num_list:
        pass

    length = 1
    max_num = -1

    for j in range(i, N-1):
        current = A[j]

        if current > max_num :
            max_num = current
        
        if A[j + 1] > max_num:
            length += 1
            
    num_list[i] = length 
    max_num_list = max(max_num_list, length)

print(max(num_list.values()))