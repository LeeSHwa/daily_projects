# https://www.acmicpc.net/problem/2920

A = input().split()

if A == ['1','2','3','4','5','6','7','8']:
    print("ascending")
elif A == ['8','7','6','5','4','3','2','1']:
    print("descending")
else:
    print("mixed")
