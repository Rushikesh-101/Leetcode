class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        


        # keep queue[0] updated as per window 
        # compare i and queue[-1] then add
        # from k-1, start appending to res


        
        res = []
        que = deque()

        for i in range(len(nums)): # i = indexes of nums : 0 1 2 3
            
            if que and que[0] <= i-k : 
                que.popleft()
            
            while que and nums[que[-1]] < nums[i] :
                que.pop()
            que.append(i)

            if i - k >= -1 :
                res.append(nums[que[0]])
            
        return res

