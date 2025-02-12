# https://www.acmicpc.net/problem/4153

while True:
    try:
        A, B, C = sorted(map(int,input().split()))

        if A == 0 and B == 0 and C == 0:
            break

        if A**2 + B**2 == C**2:
            print('right')

        else:
            print('wrong')

    except:
        break