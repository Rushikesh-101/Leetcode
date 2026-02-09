class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Simple Logic : At each index calculate the farthest you can reach

        def jump():
            if len(nums) == 1:
                return True
            idx = -1
            for i in range(len(nums)):
                if nums[i] == 0:
                    if i == len(nums)-1 and idx >= i:
                        return True
                    elif idx <= i:
                        return False
                 
                elif nums[i] != 0:
                    idx = max(idx,nums[i] + i)
            
            return True 
        
        return jump()
                 