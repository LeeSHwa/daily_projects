# https://www.acmicpc.net/problem/11723

'''
문제
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
입력
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.

둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

출력
check 연산이 주어질때마다, 결과를 출력한다.

예제 입력 1 
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
예제 출력 1 
1
1
0
1
0
1
0
1
0
1
1
0
0
0
1
0
'''
import sys
input = sys.stdin.readline

M = int(input())

bitmask = 0
# print_ans = []

for _ in range(M):
    line = input()
    parts = line.split() # 명령어 단독으로 쓰일 경우를 대비

    cmd = parts[0]

    if len(parts) == 2:
        num = parts[1]
        num = int(num)

        if cmd == 'add': bitmask |= 1 << (num-1)

        elif cmd == 'remove': bitmask &= ~(1<< (num-1))
        
        elif cmd == 'check': 
            if bitmask & (1<<(num-1)):
                sys.stdout.write('1\n')

            else: sys.stdout.write('0\n')
        
        elif cmd == 'toggle': bitmask ^= 1 << (num-1)

    else:
        if cmd == 'all':
            bitmask = (1 << 20) - 1 # 1 0000 ... - 0001 = 1111 1111 1111 1111 1111
        elif cmd == 'empty':
            bitmask = 0

# sys.stdout.write('\n'.join(print_ans)) # 이런 문제에서는 오히려 join은 메모리 피크 최대치를 엄청 높여버림