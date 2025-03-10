# https://www.acmicpc.net/problem/18110
import sys

def round_python(num): # 파이썬에서는 0.5를 반올림 할 때, 홀수면 내리고 짝수면 올리는 조금 이상한 반올림임, 그래서 0.5일 때는 무조건 올림
    if num % 1 == 0.5:
        return int(num) + 1
    
    else:
        return round(num)

def Jjajang(n, k, li): # 절사평균 구하기 위해 양 끝 단을 없앰

    if n == 0: # 만약 n이 0이면
        return 0 # 평균도 없음, 난이도는 0 / 예외처리

    # for _ in range(k): # 절사할 만큼
    #     li.pop(0) # 앞을 자르고
    #     li.pop(len(li)-1) # 맨 뒤를 자름 
    # pop은 생각보다 시간이 오래걸리나봄 
    
    ans_list = li[k:n-k] # 슬라이싱으로 간단하게 해결하니까 바로 정답이네...
    ans = round_python(sum(ans_list)/len(ans_list))

    return ans # 그리고 평균을 구한 뒤 반올림 해준다.

def bing(max_value, li): # counting sort / max_value = 최대 값, li = 리스트
    counting = [0 for _ in range(max_value + 1)] # 최대값만큼 카운팅 하기 위해 0으로 꽉 찬 배열 생성
    
    for i in range(len(li)): # 주어진 리스트의 값들을 세기 위해
        counting[li[i]] += 1 # 카운팅 리스트에 인덱스 + 1
    
    temp = [] # 임시

    for i in range(max_value+1): # 카운팅 리스트를 순회할거임
        if counting[i] != 0: # 카운팅 리스트가 0이 아니라면
            for _ in range(counting[i]): # 카운팅 리스트의 숫자만큼 순회하며
                temp.append(i) # 해당 숫자를 그만큼 출력(확장) 하면 됨
    
    return temp


n = int(sys.stdin.readline().rstrip()) # 개수 입력받기
k = round_python(n*0.15) # 절사 평균
li = [] # 임시 리스트
max_value = 30 # Counting Sort를 사용하기 위해 최대값을 정의

for _ in range(n): # 입력받을 거임
    temp = int(sys.stdin.readline().rstrip()) # 시간절약
    li.append(temp) # 임시리스트에 추가하고

sorted_list = bing(30, li) # 최대 값이 30, 그리고 입력받은 list를 정렬함

# print(sorted_list)
print(Jjajang(n, k, sorted_list)) 