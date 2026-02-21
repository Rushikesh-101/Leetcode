class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        For finding min :
        We check which half is sorted, compare sorted halfs left and unsroted halfs left with global min
        Shrink window to unsorted half
        For cases like left == mid == right, shrink both windows by one
        '''

        def min_in_sorted():
            left = 0
            right = len(nums)-1
            minn = float('inf')
            while left <= right:
                mid = left + (right-left)//2

                if nums[left] == nums[mid] == nums[right]:
                    minn = min(minn,nums[left])
                    left += 1
                    right -= 1
                elif nums[left] <= nums[mid]: # left half is sorted
                    minn = min(minn,nums[left])
                    left = mid+1
                else: # Right half is sorted
                    minn = min(minn,nums[mid])
                    right = mid-1
            
            return minn
        return min_in_sorted()



