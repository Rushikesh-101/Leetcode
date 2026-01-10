class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # Kadanes algo : for circular array
        # Will have 2 cases :
            # max sub array is within boundaries
            # max sub array is a wrap around array
        # first case : handled by normal kadane
        # second case : calculate center min sub array 
            # subtract it from total sum of nums to 
        
        

        def kadane():

            # Max sub array
            max_sum = float(-inf)
            sum = 0
            nums_total = 0

            for i in range(len(nums)):
                sum = max(nums[i], sum+nums[i])

                if sum > max_sum:
                    max_sum = sum
                nums_total += nums[i]
           

            # Min sub array
            min_sum = float(+inf)
            sum = 0
            for i in range(len(nums)):
                sum = min(nums[i], sum + nums[i])
            
                if sum < min_sum:
                    min_sum = sum

                    
            diff_calctd =  nums_total- min_sum
            if  max_sum < diff_calctd and diff_calctd != 0:
                max_sum = diff_calctd
            

            return max_sum

        return kadane()
            

        

        


