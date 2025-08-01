import sys
input = sys.stdin.readline

N = int(input())

array = [int(input().strip()) for _ in range(N)]
heap = [0]
answer = []

def sift_up(heap, index):
    while index > 1:
        parent = index // 2

        if heap[parent] < heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
        
            index = parent

        else:
            break

def push(heap, num):
    heap.append(num)
    sift_up(heap, len(heap)-1)

def sift_down(heap, index):
    length = len(heap)

    
    while True:
        left = index * 2
        right = index * 2 + 1
        biggest = index

        if left < length and heap[left] > heap[biggest]: # 부모가 더 크면 
            biggest = left

        if right < length and heap[right] > heap[biggest]:
            biggest = right

        if biggest == index:
            break
        
        heap[biggest], heap[index] = heap[index], heap[biggest]
        index = biggest

def pop(heap):
    if len(heap) == 1:
        return 0
    
    heap[1], heap[-1] = heap[-1], heap[1]
    max_value = heap.pop()

    sift_down(heap, 1)
    return max_value

for num in array:
    if num == 0:
        popped = pop(heap)
        answer.append(str(popped))
        
    else:
        push(heap, num)

print('\n'.join(answer))