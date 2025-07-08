# https://www.acmicpc.net/problem/1874

'''
문제
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

예제 입력 1 
8
4
3
6
8
7
5
2
1
예제 출력 1 
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

'''
# [1, 2, 3, 4, 5 ... ,  n] 을 가지고 push와 pop만으로 주어진 수열을 만들어야 하는 문제
# [1, 2, 3, 4, 5] -> [1, 2, 5, 3, 4]는 만들 수 없음 (push -> pop -> push -> pop -> push -> push -> push -> pop // 여기서 스택에는 3, 4만 남아있음, top은 4 고로 불가능)

# 가장 높은 숫자에 도달했을 때 부턴 숫자가 내려갈 수 밖에 없음
# 또한 4 -> 3 -> 다음으로 1, 2 이런식으로는 안됨. 4 -> 2 -> 3 이런식도 안되는데?? 무조건 인접한 수만 출력이 가능하네 3 -> 1은 불가능

# 4, 3, 6, 8, 7, 5, 2, 1
# 위치에 따라 push 및 pop의 횟수를 출력?
# 1부터 n까지 들어가니까 일단 4를 출력하려면 push * 4, pop * 1
# 그 이후 stack에는 1, 2, 3이 들어가있을건데 바로 3을 출력하니까 pop * 1
# 그 이후 6은 stack에 없으니까 stack에 6이 있을 때 까지 push * 2, pop * 1
# 8 또한 마찬가지로 push * 2, pop * 1
# 8까지 왔으면 앞으로는 pop밖에 없음 ~ 

# 안되는 조건은 어떻게 찾아야 하지?
# 일단 그냥 구현해보자
import sys

input = sys.stdin.readline

n = int(input())

answers = []
stack = []

print_ans = []

push_num = 1

for _ in range(n):
    answers.append(int(input()))

for search in answers:
    while push_num <= search:
        stack.append(push_num)
        print_ans.append("+")
        push_num += 1
    
    if stack[-1] == search:
        stack.pop()
        print_ans.append("-")
    else:
        print("NO")
        exit()

print('\n'.join(print_ans))
