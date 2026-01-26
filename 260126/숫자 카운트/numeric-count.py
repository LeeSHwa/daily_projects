N = int(input())
array = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            
            if i == j or j == k or k == i:
                continue
            
            flag = True
            
            for num, strike, ball in array:
                cnt_1 = 0
                cnt_2 = 0

                first, second, third = list(map(int, str(num)))

                if i == first : cnt_1 += 1
                if j == second: cnt_1 += 1
                if k == third : cnt_1 += 1

                if i == second or i == third: cnt_2 += 1
                if j == first or j == third : cnt_2 += 1
                if k == first or k == second: cnt_2 += 1

                if cnt_1 != strike and cnt_2 != ball:
                    flag = False
                    break
            
            if flag:
                answer += 1


print(answer)