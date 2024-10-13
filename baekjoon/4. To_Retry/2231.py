# 문제 https://www.acmicpc.net/problem/2231
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

# 출력
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

def find_constructor(N):

    digits = [int(n) for n in N] # 자리수를 구하기 위함

    # init_v = int(N) - (len(digits)-1)*9 # 생성자의 최소 범위는(분해합 - 자리수 -1) * 9 부터임
    # if int(N) < 10: # 아니 근데 왜 이게 통과가 안되는거지??? 틀린게 없는 것 같은데 허 참
    #     init_v = 0
    
    init_v = 0 # 
    
    for i in range(init_v, int(N)+1): # init_v 부터 N 까지 분해합을 구함
        temp_digit = [int(n) for n in str(i)] # i의 자리수마다 temp_digit 리스트에 저장

        # print("i ->",i,"/ i + sum(temp_digit)",i + sum(temp_digit),end=" / ")
        # for j in range(len(temp_digit)):
        #     print(temp_digit[j], end="_")
        # print(", N ->",N)

        if i + sum(temp_digit) == int(N): # 만약 i + 각 자리수의 합이 N과 같다면, 그 i가 N의 최소 생성자임
            return i # 최소 생성자 리턴

        
    return 0

ans = find_constructor(input()) # i를 리턴받음
print(ans)