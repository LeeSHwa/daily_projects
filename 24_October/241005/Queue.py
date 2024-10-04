
def Is_Queue_Full():
    global Size, front, rear, queue


    if rear == Size -1 :
        return True
    else: False
        

def Enqueue(word):
    global Size, front, rear, queue
    if Is_Queue_Full() == True:
        return print("꽉차서 안됑")
    else:
        rear += 1
        queue[rear] = word

def Is_Empty_Queue():
    global Size, front, rear, queue
    if front and rear == -1:
        return True
    else: False

def Dequeue():
    global Size, front, rear, queue
    if Is_Empty_Queue() == True:
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
Dequeue()
Enqueue("1")
Dequeue()
Enqueue("2")
Dequeue()
Enqueue("3")
Dequeue()

print(queue)


# front +=1
# data = queue[front]
# queue[front] = None
# print(f"Deque : {data}")
# print(queue)

# front +=1
# data = queue[front]
# queue[front] = None
# print(f"Deque : {data}")
# print(queue)

# front +=1
# data = queue[front]
# queue[front] = None
# print(f"Deque : {data}")
# print(queue)

# if rear == N-1:
#     print("큐가 꽉참")