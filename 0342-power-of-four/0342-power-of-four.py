class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        def power(n):
            if n == 1 or n == 4:
                return True
            
            else:
                if n%4 != 0:
                    return False
                return power(n/4)
        
        return power(n)