class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        def ispeak(mid):
            if mid == 0 and nums[mid] > nums[mid+1]:
                return True
            elif mid == len(nums)-1 and nums[mid] > nums[mid-1]:
                return True
            elif nums[mid-1] < nums[mid] > nums[mid+1]:
                return True
            else:
                return False
        def find_peak():
            left = 0
            right = len(nums)-1

            while left <= right:
                mid = left + (right-left)//2

                if ispeak(mid):
                    return mid
                else:
                    if mid == 0:
                        left = mid+1
                    elif mid == len(nums)-1:
                        right = mid-1
                    elif nums[mid-1] == nums[mid+1]:
                        left = mid+1
                        
                    elif nums[mid] < nums[mid+1]:
                        left = mid+1
                    else:
                        right = mid-1
        return find_peak()