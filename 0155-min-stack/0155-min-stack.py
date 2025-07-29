class MinStack:

    def __init__(self):
        # self.stack = []
        self.min_stack = []
        self.min = float(inf)
        self.stack = []
       

    def push(self, val: int) -> None:
        n=0


        while self.stack and self.stack[-1] < val:
            self.min_stack.append(self.stack.pop())
            n+=1
        self.stack.append(val)

        while n != 0:
            self.stack.append(self.min_stack.pop())
            n-=1
       

        self.min_stack.append(val)
        if val < self.min:
            self.min = val





            

    def pop(self) -> None:
        toRemove = 0
        n=0
        

        toRemove = self.min_stack.pop()
        print("\n this is how stack looks after popping: \n", self.min_stack)

        while self.stack and self.stack[-1] != toRemove :
           self.min_stack.append(self.stack.pop())
           n += 1
        self.stack.pop()
        print("\n removing the minstack element from stack too: \n", self.stack )


        print("\n minstack after stroing temp elements :\n", self.min_stack)
        while n != 0:
            self.stack.append(self.min_stack.pop())
            n -= 1
        
        print("\n stack after returned its element after popping \n", self.stack)

           


    def top(self) -> int:
        # if self.min_stack[-1] == -2 :
        #     return 0
        # else:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()