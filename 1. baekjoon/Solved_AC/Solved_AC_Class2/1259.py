# https://www.acmicpc.net/problem/1259


while True:
    N = input()

    flag = True

    if N == '0':
        break

    for i in range(len(N)):
        if N[i] == N[len(N)-i-1]:
            continue

        else:
            flag = False


    if flag == False:
        print('no')
        continue
    
    print('yes')

