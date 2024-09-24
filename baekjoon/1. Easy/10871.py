# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작 은수를 모두 출력하는 프로그램을 작성하시오.
# 1<= N,X <= 10,000

A = []
N = 0
X = 0

N, X = input().split(" ")
A = input().split(" ")

for i in range(0,int(N)):
    if int(A[i]) < int(X):
        print(A[i], end=" ")
    else:
        pass

