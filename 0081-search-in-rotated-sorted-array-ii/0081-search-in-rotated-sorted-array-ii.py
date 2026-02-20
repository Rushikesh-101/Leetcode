class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Problematic case : left == mid == right 
        def rotated_array():

            left = 0
            right = len(nums)-1

            while left <= right:
                mid = left + (right-left)//2

                if nums[mid] == target:
                    return True
                
                if nums[left] == nums[mid] == nums[right]:
                    left += 1
                    right -= 1

                elif nums[mid] <= nums[right]:
                    if nums[mid] < target <= nums[right]:
                        left = mid+1
                    else:
                        right = mid-1

                else:
                    if nums[left] <= target < nums[mid]:
                        right = mid-1
                    else:
                        left = mid+1
                    
                

            return False
        
        return rotated_array()
