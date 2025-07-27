# https://www.acmicpc.net/problem/17626

'''
문제 - Four Squares
라그랑주는 1770년에 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다. 어떤 자연수는 복수의 방법으로 표현된다. 예를 들면, 26은 5^2과 1^2의 합이다; 또한 4^2 + 3^2 + 1^2으로 표현할 수도 있다. 역사적으로 암산의 명수들에게 공통적으로 주어지는 문제가 바로 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내라는 것이었다. 1900년대 초반에 한 암산가가 15663 = 1252 + 62 + 12 + 12라는 해를 구하는데 8초가 걸렸다는 보고가 있다. 좀 더 어려운 문제에 대해서는 56초가 걸렸다: 11339 = 1052 + 152 + 82 + 52.

자연수 n이 주어질 때, n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램을 작성하시오.

입력
입력은 표준입력을 사용한다. 입력은 자연수 n을 포함하는 한 줄로 구성된다. 여기서, 1 ≤ n ≤ 50,000이다.

출력
출력은 표준출력을 사용한다. 합이 n과 같게 되는 제곱수들의 최소 개수를 한 줄에 출력한다.

예제 입력 1 
25
예제 출력 1 
1
'''
import math

n = int(input())

fourSquares = [4] * (n+1) # DP 저장 배열

for i in range(1, int(math.sqrt(n))+1):
    fourSquares[i*i] = 1 # 제곱수는 무조건 1

for i in range(1, n+1):
    if fourSquares[i] == 1: # 제곱수라면 패스
        continue
    
    for j in range(1, int(math.sqrt(i)) + 1):
        fourSquares[i] = min(fourSquares[i], fourSquares[i - j*j] + 1) # or fourSquares[i - j*j] + fourSquares[j * j], 하지만 j*j는 제곱수이기 때문에 무조건 1임

        if fourSquares[i] == 2: # 제곱수를 제외하면 2가 가장 작은 수임
            break  # 그러므로 반복 중단



print(fourSquares[n])
