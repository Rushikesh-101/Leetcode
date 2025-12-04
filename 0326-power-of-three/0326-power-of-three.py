class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # can be done by divind the number till its 1 
        # or multiplying three till its equal to that number
        # first approach is better cause its a shrinking solution

        def div(n):
            if n == 1:
                return True
            if n % 3 != 0 or n <= 0:
                return False
            return div(n//3)

        return div(n)