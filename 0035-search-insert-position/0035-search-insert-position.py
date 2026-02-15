class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def insert():
                
            l = 0
            r = len(nums)-1
            end = len(nums)-1

            while l<=r:
                mid = l + (r-l)//2 # to avoid integer overflow

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            if nums[mid] == target :
                return mid
            if target > nums[mid]:
                return mid+1
            else:
                return mid
            
        return insert()
        
