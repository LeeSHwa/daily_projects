''' 문제 https://www.acmicpc.net/problem/14476
정수 A가 B로 나누어 떨어지면, B는 A의 약수이고 A는 B의 배수이다.

최대공약수란 정수의 공통된 약수 중 가장 큰 수를 말한다. 예를 들어, 12와 8의 공통된 약수 1, 2, 4 중에서 가장 큰 것은 4이기 때문에 12와 8의 최대공약수는 4이다.

N개의 정수 중에서 임의의 수 K를 뺐을 때, 나머지 N-1개의 최대공약수가 가장 커지는 것을 찾는 프로그램을 작성하시오. 이때, 최대공약수는 K의 약수가 되면 안 된다.

예를 들어, 정수 8, 12, 24, 36, 48에서 8을 빼면 나머지 12, 24, 36, 48의 최대공약수는 12가 되고, 12는 빠진 수 8의 약수가 아니기 때문에 정답이 될 수 있다. 이때, 다른 수를 빼도 최대공약수가 8보다 커질 수 없다.

하지만, 8, 12, 20, 32, 36의 경우에는 그 무엇을 빼더라도 나머지 수의 최대공약수가 K의 약수가 되기 때문에, 정답을 구할 수 없다.

N개의 수가 주어졌을 때, 정수 하나를 빼서 만들 수 있는 가장 큰 최대공약수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (4 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄부터 N개의 줄에는 N개의 수가 주어진다. 각각의 수는 20억을 넘지 않는 자연수이다.

출력
첫째 줄에 정수 하나를 빼서 만들 수 있는 가장 큰 최대공약수를 출력하고, 공백을 출력한 다음 뺀 수를 출력한다. 

뺀 수를 K라고 했을 때, 나머지 수의 최대공약수가 K의 약수가 되면 안 된다.

만약 정답이 없는 경우에는 -1을 출력한다.'''

N = int(input())
GCD = {}

numbers = list(map(int,input().split()))

if len(numbers) != N:
    raise ValueError("The length of the list does not match N")

for i in range(len(numbers)):
    K = numbers.pop(i)
    
    temp = numbers[:]

    while len(temp) != 1:
        a, b = temp[0], temp[1]

        while a % b != 0:
            a,b = b, a%b

        del(temp[0])
        temp[0] = b

    if K % b == 0:
        GCD[K] = -1
    else:
        GCD[K] = b

    numbers.append(K)


ans = sorted(GCD.items(),key=lambda x : x[1])

print(ans[N-1][1],end=" ")
if ans[N-1][1] == -1:
    pass
else:
    print(ans[N-1][0])
