class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        def leftAlone():
            res = 0
            for num in nums:
                res = res ^ num
            return res
        
        return leftAlone()