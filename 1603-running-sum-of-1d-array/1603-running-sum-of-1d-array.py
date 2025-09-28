class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        sum = 0
        for i in nums:

            prefix.append(i+sum)
            sum+=i
        
        return prefix

