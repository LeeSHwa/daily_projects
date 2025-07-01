C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0]  # 첫 번째 값은 학생 수
    scores = data[1:]  # 나머지는 점수들

    average = sum(scores) / N  # 평균 계산
    count = sum(1 for score in scores if score > average)  # 평균 초과 인원 카운트

    percentage = (count / N) * 100  # 백분율 계산
    print(f"{percentage:.3f}%")