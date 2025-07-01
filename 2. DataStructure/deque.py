# deque (덱, Double-Ended Queue)
class deque:
    def __init__(self, max_size = 100):
        self.MAX_SIZE = max_size
        self.deq = [None] * self.MAX_SIZE
        self.front = 0
        self.rear = 0
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear + 1) % self.MAX_SIZE == self.front
    
    def add_rear(self, x):
        if self.is_full():
            print("ERROR - deq is full!")
            return
        self.rear = (self.rear + 1) % self.MAX_SIZE
        self.deq[self.rear] = x
        
    def add_front(self, x):
        if self.is_full():
            print("ERROR - deq is full!")
            return
        self.deq[self.front] = x
        self.front = (self.front - 1 + self.MAX_SIZE) % self.MAX_SIZE
        
    def del_front(self):
        if self.is_empty():
            print("ERROR - deq is empty!")
            return None
        self.front = (self.front + 1) % self.MAX_SIZE
        return self.deq[self.front]

    def del_rear(self):
        if self.is_empty():
            print("ERROR - deq is empty!")
            return None
        item = self.deq[self.rear]
        self.rear = (self.rear - 1 + self.MAX_SIZE) % self.MAX_SIZE
        return item

    def get_front(self):
        if self.is_empty():
            print("ERROR - deq is empty!")
            return None
        return self.deq[(self.front + 1) % self.MAX_SIZE]
    
    def get_rear(self):
        if self.is_empty():
            print("ERROR - deq is empty!")
            return None
        return self.deq[self.rear]

    def print_deque(self):
        if self.is_empty():
            print("ERROR - deque is empty!")
            return
        i = (self.front + 1) % self.MAX_SIZE
        while i != self.rear:
            print(self.deq[i], end=' ')
            i = (i + 1) % self.MAX_SIZE
        print(self.deq[i])

dq = deque()

dq.add_front(1)
dq.add_rear(2)
dq.add_rear(3)
dq.add_front(0)
dq.print_deque()

dq.del_front()
dq.del_rear()
dq.print_deque()