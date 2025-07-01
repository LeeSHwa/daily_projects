N = int(input())  # 설탕의 양

count = 0

while N >= 0:
    if N % 5 == 0:  # 5kg 봉지로 나누어 떨어지면
        count += N // 5  # 5kg 봉지의 개수를 세고 출력
        print(count)
        break
    N -= 3  # 5로 나누어 떨어지지 않으면 3kg 봉지를 하나 사용
    count += 1  # 3kg 봉지 개수 증가
else:
    print(-1)  # 정확하게 나눌 수 없을 때