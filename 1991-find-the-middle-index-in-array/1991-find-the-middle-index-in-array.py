class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # Leftmost, so whereever we find it while traversing from left to right, we return it immediately 
        n = len(nums)
        prefix = [0]*n
        prefix[0] = 0

        total = sum(nums)

        if (total - nums[0]) == 0:
            return 0
        for i in range (1,n):
            prefix[i] = prefix[i-1] + nums[i-1]
            if prefix[i] == (total - prefix[i]) - nums[i]:
                return i
            
        return -1