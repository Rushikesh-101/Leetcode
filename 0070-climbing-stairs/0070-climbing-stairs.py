class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {'1':1,'2':2}

        def climb(n):
            if n == 0 :
                return 1
            if str(n) in dp:
                return dp[str(n)]
            first_way = 0
            second_way = 0


            if n >= 2 :
                second_way = climb(n-2)

            if n >= 1 :
                first_way = climb(n-1)
            dp[str(n)] = first_way + second_way
            return first_way + second_way

        return climb(n)
        