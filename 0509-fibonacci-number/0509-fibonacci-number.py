class Solution:
    def fib(self, n: int) -> int:
        
        def recurr(x):
            if x == 0 or x == 1:
                return 0 if x==0 else 1

            x = recurr(x-1)+recurr(x-2)
            return x
        
        return recurr(n)

        '''

        Above code recomputes value :
        Ex : Your Fibonacci recursion calls the same values repeatedly:

            fib(5) calls fib(4) and fib(3)
            fib(4) calls fib(3) and fib(2)
            fib(3) calls fib(2) and fib(1)
            ...and so on
            You end up recomputing fib(3) multiple times. 

        Instead store computed values in dict, check if resusable.

        '''
        storage = {}

        def recurr(x):
            if x in storage:
                return storage[x]

            if x == 0 or x == 1:
                return 0 if x==0 else 1

            result = recurr(x-1)+recurr(x-2)
            storage[x] = result
            return result
        
        return recurr(n)
        