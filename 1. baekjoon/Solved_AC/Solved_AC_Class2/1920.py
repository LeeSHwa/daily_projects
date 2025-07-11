# https://www.acmicpc.net/problem/1920 수 찾기

'''
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

예제 입력 1
5
4 1 5 2 3
5
1 3 7 9 5

예제 출력 1
1
1
0
0
1

'''

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

A = set(map(int, input().split())) # 자료 탐색시에는 set형이 최고임 / hash table 구조라 연산들이 모두 평균적으로 O(1) 임

M = int(input())

Num = list(map(int, input().split()))

result = []

# 즉시 출력하는 것 보단 나중에 join을 활용하여 출력하는게 메모리 부분에서 훨씬 유리
for i in Num:
    if i in A:
        # print('1\n')
        result.append('1\n')
    # else: print('0\n')
    else: result.append('0\n')
    

print(''.join(result))