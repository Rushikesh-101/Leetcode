# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left = 0
        right = n
        middle = ( left + right )//2
        
        while left < right :
            
           

            if isBadVersion(middle) == True :

                right = middle
                middle = ( left + right )//2
            
            elif isBadVersion(middle) == False :

                left = middle + 1
                middle = ( left + right )//2

            

        if isBadVersion(middle) == True and isBadVersion(middle -1) == False :

            return middle

        elif isBadVersion(middle) == False and isBadVersion(middle +1) == True :

            return middle+1
            