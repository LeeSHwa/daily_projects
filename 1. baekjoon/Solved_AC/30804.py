# https://www.acmicpc.net/problem/30804
from collections import defaultdict

N = int(input())

candies = input().split()

left = right = 0

longgest = 0

while True:
    slice = candies[left:right+1]
    
    set_slice = set(slice)

    len_set = len(set_slice)



    if len_set <= 2 and right < len(candies):
        right += 1
        if len(slice) > longgest:
            longgest = len(slice)
    else:
        left += 1 
    
    if right == left:
        break

print(longgest)
    