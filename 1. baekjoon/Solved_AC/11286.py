# https://www.acmicpc.net/problem/11286

# 문제 - 절댓값 힙

N = int(input())

heap = [None]

def up(index):
    parrent = index // 2
    
    if abs(heap[parrent]) > abs(heap[index]) or (abs(heap[parrent] == abs[heap[index]] and heap[parrent] > heap[index])):
        heap[parrent], heap[index] = heap[index], heap[parrent]

def push(num):
    heap.append(num)

    if len(heap) == 2:
        pass
    else:
        up(len(heap) - 1)

def down():
    
    current = 1

    while current < len(heap):
        left = current * 2
        right = current * 2 + 1

        if abs(heap[current]) > abs(heap[left]) or (abs(heap[current] == abs[heap[left]] and heap[current] > heap[left])):
            heap[current], heap[left] = heap[left], heap[current]
        
        if abs(heap[current]) > abs(heap[left]) or (abs(heap[current] == abs[heap[right]] and heap[current] > heap[right])):
            heap[current], heap[left] = heap[left], heap[current]
        


def pop(length):
    heap[1], heap[length] = heap[length], heap[1]
    popped = heap.pop()
    down()

    return popped
    

for _ in range(N):
    num = int(input())
    
    if num != 0:
        push(num)
    
    else:
        if len(heap) == 1:
            print(0)
            continue
        print(pop(len(heap)))