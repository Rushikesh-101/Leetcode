class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at every element  self val and prev best sub array + self val, if added val is better, then add it and send to next element, if non added val is better, 
    
        # KADANES ALGO : max(nums[i], nums[i]+sum)

        def maxi_sub():
            total_max = float(-inf)
            sum = 0

            for i in range(0,len(nums)):
                sum = max(nums[i],nums[i] + sum)
                
                if sum > total_max:
                    total_max = sum
            
            return total_max
            

        return maxi_sub()
        