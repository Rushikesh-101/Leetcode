class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = {}

        def isbst(x):
            if x in dp:
                return dp[x]
            else :
                total = 0
                if x == 1 or x == 0:
                        return 1
                for i in range(1,x+1):
                    
                    left = isbst(i-1)
                    right = isbst(x-i)

                    total += left*right
                dp[x] = total
                return total
        
        return isbst(n)
        