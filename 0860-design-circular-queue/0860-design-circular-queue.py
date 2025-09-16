class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k       # initialise queue with filled none values, else assignment by index fails
        self.front = 0
        self.rear = -1
        self.k = k
        self.currSize = 0
    def enQueue(self, value: int) -> bool:

        if self.currSize == self.k:
            return False

        else:
            self.rear = (self.rear+1)%self.k
            self.queue[self.rear] = value
            self.currSize += 1
            return True

    def deQueue(self) -> bool:
        
        if self.currSize == 0:
            return False
        else:
            self.queue[self.front] = None           # ( self.front = None ( destroys the pointer ))
            self.front = (self.front+1)%self.k      # (self.queue[self.front] = None (destroys val))
            self.currSize -= 1
            return True

    def Front(self) -> int:
        if self.currSize > 0:
            value = self.queue[self.front]
            return value
        else :
            return -1
    def Rear(self) -> int:
        if self.currSize > 0:
            value = self.queue[self.rear]
            return value
        else :
            return -1


    def isEmpty(self) -> bool:
        if self.currSize == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.currSize == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()