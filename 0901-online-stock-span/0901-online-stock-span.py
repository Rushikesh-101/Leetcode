class StockSpanner:

    def __init__(self):
        self.mono = []
        self.ele_id = -1
        self.list = []
    def next(self, price: int) -> int:

        self.list.append(price)
        self.ele_id += 1
       
        while self.mono and self.list[self.mono[-1]] <= price:
            self.mono.pop()
        if self.mono:
            pops = self.ele_id - self.mono[-1] -1
        else :
            pops = self.ele_id

        self.mono.append(self.ele_id)

        return pops+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)









        