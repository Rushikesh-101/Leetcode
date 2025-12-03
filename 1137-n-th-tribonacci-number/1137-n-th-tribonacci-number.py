class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def compute(x):

            if x in memo:
                return memo[x]
            
            elif x == 0 or x == 1 or x == 2 :
                if x == 0:
                    return 0
                if x == 1:
                    return 1
                if x == 2 :
                    return 1
            
            memo[x] = compute(x-1)+compute(x-2)+compute(x-3) 
            return memo[x]
        
        return compute(n)