class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        # just like pivot_index
        # no prefix suffix list required
        # only one variable, total, and a loop
        def left_right_diff():
            total = sum(nums)
            left = 0
            result = [0]*len(nums)
            for i in range(len(nums)):
                result[i] = abs(left - (total-left-nums[i]))
                left += nums[i]
            return result
        
        return left_right_diff()