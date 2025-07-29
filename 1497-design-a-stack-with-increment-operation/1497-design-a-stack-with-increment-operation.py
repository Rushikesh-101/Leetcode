class CustomStack:

    def __init__(self, maxSize: int):
        self.cusStack = []
        self.limit = maxSize


    def push(self, x: int) -> None:
        if len(self.cusStack) < self.limit :
            self.cusStack.append(x)
        # print("\n this is how stack looks after append \n", self.cusStack)

    def pop(self) -> int:
        if self.cusStack :
            return self.cusStack.pop()
        else :
            return -1
        # print("\n this is how stack looks after pop \n", self.cusStack)

    def increment(self, k: int, val: int) -> None:
        
        if len(self.cusStack) < k :
            k = len(self.cusStack) 

        incr = 0
        while k != 0:
            self.cusStack[incr] += val
            incr+=1
            k-=1
        

            

            # print("\n this is how stack looks after inc using else \n", self.cusStack)
        


        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)