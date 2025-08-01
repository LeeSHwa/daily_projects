import sys
input = sys.stdin.readline

N = int(input())

array = [int(input().strip()) for _ in range(N)]
heap = [None] # 0번 인덱스는 None으로 지정 / 추후 인덱스 계산을 쉽게하기 위함
answer = [] 

def sift_up(heap, index): # push 이후 부모-자식 노드 비교하여 정렬하는 함수
    while index > 1: # 1-based
        parent = index // 2
        # 부모는 (자식 인덱스 // 2)임 (ex. 4, 5 -> 2번이 부모노드)

        # 예: 힙 트리 구조 (1-based 인덱스)
        #       5 (index 1)
        #     /    \
        #   4(2)   3(3)
        #  /  \
        #1(4) 3(5)

        # 자식 노드가 부모노드보다 크다면 둘의 위치를 바꿔줌
        if heap[parent] < heap[index]: 
            heap[parent], heap[index] = heap[index], heap[parent]
        
            index = parent     # 바꾼 후 해당 노드의 위치를 index로 재설정

        else:                  # 만약 부모노드가 자식노드보다 크면
            break              # 바꿀필요 없음, break

def push(heap, num):           # 새로운 값을 추가하는 함수
    heap.append(num)           # 일단 맨 끝 인덱스에 값을 추가
    sift_up(heap, len(heap)-1) # (크기 - 1) 인덱스를 기준으로 sift up

def sift_down(heap, index):
    length = len(heap)

    while True:
        left = 2 * index       # 왼쪽 자식 인덱스
        right = 2 * index + 1  # 오른쪽 자식 인덱스
        biggest = index        # 부모 노드 인덱스 (기준)

        # 왼쪽 자식이 유효하며, 현재 최대값보다 크면 최대값 갱신
        if left < length and heap[left] > heap[biggest]:
            biggest = left

        # 오른쪽 자식이 유효하며, 현재 최대값보다 크면 최대값 갱신
        if right < length and heap[right] > heap[biggest]:
            biggest = right

        # 변경 없으면 반복 종료
        if biggest == index:
            break

        # 최대값 위치 교환
        heap[biggest], heap[index] = heap[index], heap[biggest]
        index = biggest


def pop(heap): # 1번째 인덱스와 가장 마지막 인덱스의 값을 바꾼 후, 기존 1번째 인덱스 값을 pop 해주는 함수
    if len(heap) == 1:
        return 0
    
    heap[1], heap[-1] = heap[-1], heap[1]
    max_value = heap.pop()

    sift_down(heap, 1) # 바꿨으니 sift down
    return max_value   # popped value == max value

# 실제 실행부분
for num in array:      
    if num == 0:                 
        popped = pop(heap)         
        answer.append(str(popped)) # join 연산을 위해 string 형으로 형변환
        
    else: 
        push(heap, num)  # 0이 아닌 수는 모두 push

print('\n'.join(answer)) # 정답 출력