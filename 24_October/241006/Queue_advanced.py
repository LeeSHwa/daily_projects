# 선형 큐의 기본 성질을 무시하고 만든 코드
# 선형큐는 한 번 공간이 채워지면 끝!!임
# 내 방식은 원형큐에 가까움 


def Is_Queue_Full():
    global Size, rear

    return rear == Size -1

def Enqueue(word):
    global Size, front, rear, queue

    if Is_Queue_Full():
        return print("꽉차서 안됑")
    else:
        if Is_Queue_Empty():
            front = rear = -1
        rear += 1
        queue[rear] = word


def Is_Queue_Empty():
    global front, rear
    return front == rear

def Dequeue():
    global Size, front, rear, queue

    if Is_Queue_Empty() == True:
        front = rear = -1
        return print("얜 비어서 안됑")

    else:
        front += 1
        data = queue[front]
        queue[front] = None
        print(data ," <- 얘 없어짐")
        return False

Size = 5
queue = [None for _ in range(Size)]

rear = front = -1

Enqueue('First')
Enqueue('Second')
Enqueue('Third')

Dequeue()
Dequeue()
Dequeue()

Enqueue('Fourth')
Enqueue('Fifth')

print(queue)
