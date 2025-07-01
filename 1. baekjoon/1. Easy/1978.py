# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

N = int(input())

M = list(map(int,input().split(" ")))

if len(M) != N:
    raise ValueError(f"입력된 숫자의 개수가 {N}개가 아닙니다.")

Prime_value = []

for i in M:
    cnt = 0
    for j in range(2,i):
        if i % j == 0 :
            break
        else:
            cnt += 1

    if cnt == i - 2:
        Prime_value.append(i)

ans = len(Prime_value)
print(ans)