class Solution:
    def fib(self, n: int) -> int:
        
        def recurr(x):
            if x == 0 or x == 1:
                return 0 if x==0 else 1

            x = recurr(x-1)+recurr(x-2)
            return x
        
        return recurr(n)
