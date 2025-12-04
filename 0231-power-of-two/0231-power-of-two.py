class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        def power(x):

            if x == 1:
                return True
            
            if x % 2 != 0 or x <= 0:
                return False

            return power(x//2)
        
        return power(n)