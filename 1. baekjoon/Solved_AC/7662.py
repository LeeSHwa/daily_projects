# https://www.acmicpc.net/problem/7662

# 문제 - 이중 우선순위 큐
import sys
input = sys.stdin.readline   
        
def push(list, input_num, type):
    list.append(input_num)
    sift_up(list, len(list), type)

def sift_up(list, length, type):
    current = length - 1
    
    while True:
        parent = current // 2

        if type == 'min':
            if current > 1 and list[current] < list[parent]:
                list[current], list[parent] = list[parent], list[current]
                current = parent
            else:
                return
        
        else:
            if current > 1 and list[current] > list[parent]:
                list[current], list[parent] = list[parent], list[current]
                current = parent
            else:
                return

def pop(list, type):
    list[1], list[-1] = list[-1], list[1]
    popped = list.pop()
    sift_down(list, type)
    
    return popped

def sift_down(list, type):
    current = 1
    maximum_index = len(list)
    
    while True:
        left = current * 2
        right = current * 2 + 1

        temp = current
        
        if type == 'min':
            
            if 0 < left < maximum_index:
                if list[current] > list[left]:
                    list[current], list[left] = list[left], list[current]
                    temp = left

            if 0 < right < maximum_index:
                if list[current] > list[right]:
                    list[current], list[right] = list[right], list[current]
                    temp = right
            
            if current == temp:
                return
            else:
                current = temp

        else:
                    
            if 0 < left < maximum_index:
                if list[current] < list[left]:
                    list[current], list[left] = list[left], list[current]
                    temp = left

            if 0 < right < maximum_index:
                if list[current] < list[right]:
                    list[current], list[right] = list[right], list[current]
                    temp = right  

            if current == temp:
                return
            else:
                current = temp

# 테스트 케이스 개수
T = int(input()) 

for _ in range(T):

    # 커맨드 개수
    k = int(input())

    # 큐 초기화
    min_q = [None]
    max_q = [None]

    # 교차검증용
    dictionary = {}

    for _ in range(k):
        command, num = input().split()
        num = int(num)
        
        # if len(min_q) > 1:
        #     tem = min_q[1]
        #     if dictionary[tem] < 1:
        #         pop(min_q, 'min')
    
        # if len(max_q) > 1:
        #     tem = max_q[1]
        #     if dictionary[tem] < 1:
        #         pop(max_q, 'max')
            
        
        # 삽입
        if command == 'I':
            push(min_q, num, 'min')
            push(max_q, num, 'max')
            # print(f"Push min : {min_q}")
            # print(f"Push max : {max_q}")

            if num in dictionary.keys():
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        #삭제
        else:
            if len(min_q) == 1 or len(max_q) == 1:
                pass
            else:
                if num == 1:

                    while max_q and dictionary.get(max_q[1], 0) == 0:
                        pop(max_q, 'max')

                    popped = pop(max_q, 'max')
                    dictionary[popped] -= 1
                    # print(f"Delete max : {max_q}")
                else:
                    
                    while min_q and dictionary.get(min_q[1], 0) == 0:
                        pop(min_q, 'min')

                    popped = pop(min_q, 'min')
                    dictionary[popped] -= 1
                    # print(f"Delete min : {min_q}")
    
    if len(max_q) == 1 or len(min_q) == 1:
        print("EMPTY")
    else:
        print(max_q[1], min_q[1])