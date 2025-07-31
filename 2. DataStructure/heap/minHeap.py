N = int(input())

array = [int(input()) for _ in range(N)]

heap = [0]

def sift_up(heap, idx):
    while idx > 0:
        parent = idx // 2        
        if heap[parent] <= heap[idx]: # 추가된 노드가 부모 노드보다 크거나 같으면
            break # 바꿀 필요가 없음, 브레이크

        heap[parent], heap[idx] = heap[idx], heap[parent] # 작으면 부모-자식 위치 교체
        idx = parent

def push(heap, x):
    heap.append(x)
    sift_up(heap, len(heap) - 1)

def sift_down(heap, idx):
    length = len(heap)

    while True:
        left = 2 * idx 
        right = 2 * idx + 1
        smallest = idx
        
        if left < N and heap[left] < heap[smallest]:
            smallest = left
        
        if right < N and heap[right] < heap[smallest]:
            smallest = right
        
        if smallest == idx:
            break
        
        heap[smallest], heap[idx] = heap[idx], heap[smallest]
        idx = smallest

def pop(heap):
    if len(heap) == 1:
        return 0
    
    heap[1], heap[-1] = heap[1], heap[-1]
    min_val = heap.pop()
    sift_down(heap, 1)

    return min_val

for num in array:
    if num == 0:
        ans = pop(heap)
        print(ans)
    
    else:
        push(heap, num)