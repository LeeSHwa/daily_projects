# https://www.acmicpc.net/problem/11053

# 문제 - 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

# 최소값은 무조건 1이니까 1로 dp배열 초기화
dp = [1] * N

# A[i]가 최대라고 가정했을 때의 값들을 DP에 넣을거임
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
    # temp_count = 0

    # A[i] 보다 작은 값만 임시로 리스트업
    # temp_list = [x for x in A if x < A[i]]

    # 만약 A[i]보다 작은 값이 없다면 자기 자신만이니까 pass
    # if len(temp_list) == 0:
    #     continue

    # 중복 제거 
    # unique = set()
    # unique_list = [x for x in temp_list if x not in unique and not unique.add(x)]

    # A[0] 부터 A[i-1]까지 (i-시작점)번 만큼 반복해서 시작점에 따른 count 값을 list에 append
