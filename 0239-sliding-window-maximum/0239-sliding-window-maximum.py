class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque

        # keep queue[0] updated as per window 
        # compare i and queue[-1] then add
        # from k-1, start appending to res
        def slide():
            result = []
            queue = deque()
            
            for i in range(len(nums)):
                
                while queue and queue[0] < (i-k)+1:
                    queue.popleft()
                
                while queue and nums[queue[-1]] < nums[i]:
                    queue.pop()
                queue.append(i)
            
                if i >= k-1:
                    result.append(nums[queue[0]])
            
            return result
        
        return slide()
                
        
        

