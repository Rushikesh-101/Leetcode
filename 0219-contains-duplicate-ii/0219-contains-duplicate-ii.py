class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        exists = set()
        r = 0
        while r < len(nums):
            if r > k:
                exists.remove(nums[r-(k+1)])
            
            if nums[r] in exists:
                return True
            else:
                exists.add(nums[r])
                r += 1
    
        return False

