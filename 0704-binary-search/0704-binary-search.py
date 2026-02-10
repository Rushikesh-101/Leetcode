class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def BS():
            l = 0
            r = len(nums)-1

            if nums[l] == target:
                return l
            elif nums[r] == target: 
                return r
            
            while l+1 != r and l < r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid
                else:
                    r = mid
                
            if nums[l] == target:
                return l
            elif nums[r] == target: 
                return r
            else:
                return -1
        
        return BS()
            
                
            

            