'''
문제 https://www.acmicpc.net/problem/1181
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
단, 중복된 단어는 하나만 남기고 제거해야 한다.

입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다.
'''

N = int(input())
words = []

for i in range(N):
    words.append(input())

dict_words = {word:len(word) for word in words} # { : } 형태가 dictionary 그 자체임, comprehension으로 요소 : 요소의 길이를 매칭시켜 주었음

sorted_words = dict(sorted(dict_words.items(),key = lambda x : x[1])) # items() -> (키, 값)인 튜플 형태로 변환 / key -> 어떤 걸 기준으로 할 것인지

print(sorted_words)

list_keys = list(sorted_words.keys())

print(list_keys)

for i in range(N):
    
    while j != N+1:
        tem = len(list_keys[1])

        if len(list_keys[1]) == tem:     
            j+=1