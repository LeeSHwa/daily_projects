# 1. 입력 받기
N = int(input())
words = []  # 단어를 저장할 리스트

# 2. N개의 단어 입력 받기
for _ in range(N):
    word = input().strip()  # 단어 입력 후 공백 제거
    if word not in words:  # 중복 방지
        words.append(word)

# 3. 정렬하기 (길이 기준 -> 사전순)
words.sort(key=lambda x: (len(x), x))  # 튜플로 정렬

# 4. 정렬된 단어 출력
for word in words:
    print(word)