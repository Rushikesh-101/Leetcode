class MyCircularDeque:

    def __init__(self, k: int):
        self.deq = [None]*k
        self.k = k
        self.front = 0
        self.rear = -1
        self.cap = 0

    def insertFront(self, value: int) -> bool:
        if self.cap == self.k:
            return False

        elif self.front == 0 and self.cap < self.k :
            self.front = self.k-1
            self.deq[self.front] = value
            self.cap += 1
            return True

        elif self.front != 0 and self.cap < self.k :
            self.front = self.front -1 
            self.deq[self.front] = value
            self.cap += 1
            return True



    def insertLast(self, value: int) -> bool:
        if self.cap == self.k:
            return False
        else :
            self.rear = (self.rear+1) % self.k
            self.deq[self.rear] = value
            self.cap += 1
            return True



    def deleteFront(self) -> bool:
        if self.cap == 0:
            return False
        else :
            self.deq[self.front] = None
            self.front = (self.front + 1) % self.k
            self.cap -= 1
            return True

    def deleteLast(self) -> bool:
        if self.cap == 0:
            return False

        elif self.rear == 0:
            self.rear = self.k-1
            self.cap -= 1
            return True

        else :
            self.deq[self.rear] = None
            self.rear -= 1
            self.cap -= 1
            return True

    def getFront(self) -> int:
        if self.cap == 0 :
            return -1

        else :
            val = self.deq[self.front]
            return val

    def getRear(self) -> int:
        if self.cap == 0 :
            return -1

        else :
            val = self.deq[self.rear] 
            return val

    def isEmpty(self) -> bool:
        if self.cap == 0:
            return True
        else :
            return False

    def isFull(self) -> bool:
        if self.cap == self.k:
            return True
        else : 
            return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()