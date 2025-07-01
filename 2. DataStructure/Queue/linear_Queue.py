# 큐는 FIFO(First in First out) 구조를 가진 자료구조이다.

queue = []
rear = front = -1 # rear = 꼬리, front = 머리

SIZE = 5 # Queue의 길이

queue = [None for _ in range(SIZE)] # 길이 N의 Queue 생성

def Is_Queue_Full():
    global rear, SIZE

    return rear == SIZE-1 # rear가 길이 -1 번째 위치라면, 큐가 모두 꽉 찬 것임

def Enqueue(word):
    global queue, rear, front
    
    if Is_Queue_Full(): 
        print("Queue is full")
        return
    else:
        rear += 1
        queue[rear] = word

def Is_Queue_Empty():
    global rear, front

    return rear == front

def Dequeue():
    global rear, front, queue

    if Is_Queue_Empty():
        print("Queue is empty")
        return
    else:
        front += 1
        data = queue[front]
        print(data,"<- is deleted")
        queue[front] = None

Enqueue("First")
Enqueue("Second")
Enqueue("Third")

print(queue)

Dequeue()
Dequeue()
Dequeue()

print(queue)

Enqueue("Fourth")
Enqueue("Fifth")

print(queue)
