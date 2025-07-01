def my_replace(original, old, new):
    result = ""
    i = 0
    while i < len(original):
        # old 패턴이 현재 위치에서 시작하는지 확인
        if original[i:i+len(old)] == old:
            result += new  # 패턴이 있으면 new로 치환
            i += len(old)  # 패턴 길이만큼 인덱스를 건너뜀
        else:
            result += original[i]  # 패턴이 없으면 그대로 문자 추가
            i += 1
    return result

# 크로아티아 알파벳 리스트 (여러 패턴)
croatia = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']

# 입력받은 단어
word = input()

# 각 크로아티아 알파벳을 '*'로 치환
for alphabet in croatia:
    word = my_replace(word, alphabet, '*')

print(len(word))  # 결과 출력