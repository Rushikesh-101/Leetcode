class Solution:
    def fib(self, n: int) -> int:
        
        def recurr(x):
            if x > 1:
                x = recurr(x-1)+recurr(x-2)
            elif x == 0:
                return 0
            elif x == 1:
                return 1
            return x
        
        return recurr(n)
