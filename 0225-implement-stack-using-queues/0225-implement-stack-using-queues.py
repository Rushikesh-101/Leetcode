class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []


    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.q1 :
            return self.q1.pop()
        # if len(self.q1) > 1:
        #     while len(self.q1) != 1:
        #         self.q2.append(self.q1.pop())
        #     return self.q1.pop()
        #     while self.q2:
        #         self.q1.append(self.q2.pop())
        # elif len(self.q1) == 1:
        #     return self.q1


    def top(self) -> int:
        if self.q1:
            res = self.q1.pop()
            print(self.q1)
            print(res)
            self.q1.append(res)
            return res
            

            # print("q1 before while in top:",self.q1)
            # while len(self.q1) != 1:
            #     self.q2.append(self.q1.pop())
            # print("q1 after while in top:",self.q1)
            
            # res = self.q1.pop()
            # self.q2.append(res)
            # print("q2 after while in top:",self.q2)

            # return res
            # while self.q2 :
            #     self.q1.append(self.q2.pop())

    def empty(self) -> bool:

        if len(self.q1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()