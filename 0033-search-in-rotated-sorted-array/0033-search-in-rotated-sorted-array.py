class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Double Binary Search approach
        # Binary search for pivot
        # Divide nums into 2 sorted halves
        # search for target by BS on both of them

        # Another approach(Optimal)
        # At each point we check which half is sorted
        # We check if mid can exist in that sorted half
        # If yes, we reduce pointers to that half else we reduce them to other half.

        def half_mad():

            left = 0
            right = len(nums)-1

            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid

                if nums[left] <= nums[mid]:# left half is sorted
                    if nums[left] <= target < nums[mid] :
                        right = mid-1
                    else:
                        left = mid+1
                else:# right half is sorted
                    if nums[mid] < target <= nums[right]:
                        left = mid+1
                    else:
                        right = mid-1

            return -1
        
        return half_mad()
                    
