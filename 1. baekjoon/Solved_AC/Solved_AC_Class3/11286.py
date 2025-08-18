# https://www.acmicpc.net/problem/11286

# 문제 - 절댓값 힙
import sys
input = sys.stdin.readline

N = int(input())

heap = [None]

def up(index):
    
    while index > 1:
        parent = index // 2

        if (abs(heap[parent]), heap[parent]) > (abs(heap[index]), heap[index]):

            heap[parent], heap[index] = heap[index], heap[parent]

            index = parent
        else:
            break

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
        temp = current

        if 0 <= left < len(heap) and\
            (abs(heap[temp]), heap[temp]) > (abs(heap[left]), heap[left]):
                temp = left

        if 0 <= right < len(heap) and\
            (abs(heap[temp]), heap[temp]) > (abs(heap[right]), heap[right]):
                temp = right


        if temp == current:
            break
        else:
            heap[current], heap[temp] = heap[temp], heap[current]
            current = temp


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

        print(pop(len(heap) - 1))