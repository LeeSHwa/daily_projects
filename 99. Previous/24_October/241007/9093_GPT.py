# https://www.acmicpc.net/problem/9093
# slicing, join 숙지

T = int(input())

for _ in range(T):
    sentence = input().split()  # 입력된 문장을 공백 기준으로 단어별로 나눔
    # 각 단어를 뒤집어서 다시 출력
    reversed_words = [word[::-1] for word in sentence]  # 각 단어를 뒤집음
    print(" ".join(reversed_words))  # 단어를 다시 공백으로 구분해서 출력
