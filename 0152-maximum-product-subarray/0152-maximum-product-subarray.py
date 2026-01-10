class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def productKadane():
            total_sum = float(-inf)

            prev_ngtv = nums[0]
            prev_pstv = nums[0]
            if total_sum < prev_pstv:
                total_sum = prev_pstv

            for i in range(1,len(nums)):

            
                # POSITIVE CASE
                if nums[i] > 0:
                    new_pos = max(prev_pstv*nums[i], nums[i])
                    new_neg = min(prev_ngtv*nums[i], nums[i])

                # NEGATIVE CASE
                elif nums[i] <= 0:
                    new_pos = max(prev_ngtv*nums[i], nums[i])
                    new_neg = min(prev_pstv*nums[i], nums[i])
                
                if new_pos > total_sum:
                    total_sum = new_pos

                prev_ngtv = new_neg
                prev_pstv = new_pos

            return total_sum
        
        return productKadane()


