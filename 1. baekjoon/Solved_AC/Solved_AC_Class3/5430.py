# https://www.acmicpc.net/problem/5430

# 문제 - AC
from collections import deque

T = int(input())

for _ in range(T):
    error_flag = False
    
    p = input().rstrip() # 문자열이여서 굳이 list로 관리하지 않아도 됨
    n = int(input())
    
    if n > 0:
        array = deque(input().strip('[]').split(','))
    else:
        array = deque()
        input() # 똥빼주기? ㅋㅋ
    # temp = input().strip('[]')     # 양 쪽 대괄호 없애고
    # array = deque(temp.split(',')) # 반점을 기준으로 split
    
    is_reversed = False            # array가 반전되었는지 확인하기 위한 플래그

    for command in p:
        if command == 'D':         # command가 D인데
            if len(array) == 0:    # 문자열이 비어있다면
                error_flag = True  # 에러플래그 = True
                break              # 의미없는 반복은 그만

            else:
                if is_reversed:      # 만약 뒤집힌 상태면
                    array.pop()      # 뒤에서 빼오고
                else:
                    array.popleft()  # 아니라면 앞에서 빼오기

        elif command == 'R':
            is_reversed = not is_reversed # toggle

    if is_reversed:
        array.reverse()
    
    if error_flag:
        print('error')
    else:
        print('[' + ','.join(array) + ']')