# https://www.acmicpc.net/problem/2751

'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys
input = sys.stdin.readline

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))

num.sort()

# for i in num: # 메모리 초과 가능성 있음
#     print(i)

sys.stdout.write('\n'.join(map(str, num)) + '\n') # join은 str형만 가능