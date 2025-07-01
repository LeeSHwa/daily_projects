SIZE = 5 #int(input())

queue = [None for _ in range(SIZE)]

rear = front = 0

def Is_Queue_Full():
    global SIZE, queue, rear, front
    return (rear + 1) % SIZE == front

def Is_Queue_Empty():
    global rear, front
    return rear == front

def Enqueue(word):
    global SIZE, queue, rear, front
    
    if Is_Queue_Full():
        print("Queue is full")
        return
    else: 
        rear = (rear + 1) % SIZE
        queue[rear] = word
        print(word, "is enqueued")
        print('->',queue)
    
def Dequeue():
    global SIZE, queue, rear, front

    if Is_Queue_Empty():
        print("Queue is empty")
        rear = front = 0
        return
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        print(data,("<- is deleted"))
        queue[front] = None

Enqueue("First")
Enqueue("Second")
Enqueue("Third")
Enqueue("Fourth")
Enqueue("Fourth")

Dequeue()
Enqueue("dumb")
Dequeue()
Dequeue()

Enqueue("Fifth")
Enqueue("Sixth")
Enqueue("Seventh")

Dequeue()

Enqueue("Eighth")