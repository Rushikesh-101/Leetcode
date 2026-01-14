class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_count = 0
        curr_count = 0
        flips = k
        right = 0
        left = 0

        for right in range(len(nums)):

            if nums[right] == 1:
                curr_count += 1

            elif nums[right] == 0 and flips:
                flips -= 1
                curr_count += 1

            

            else:
                while nums[left] != 0:
                    curr_count -= 1
                    left += 1
                curr_count -= 1
                left += 1
                curr_count += 1
            
            max_count = max(max_count,curr_count)
        
        return max_count
