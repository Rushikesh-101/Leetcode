class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def minFlips():
            # XORing both so set bits indicate difference

            diff = start ^ goal

            # Use n&(n-1) to count number of set bits
            count = 0
            while diff:
                diff = diff & (diff-1)
                count += 1
            
            return count
        
        return minFlips()