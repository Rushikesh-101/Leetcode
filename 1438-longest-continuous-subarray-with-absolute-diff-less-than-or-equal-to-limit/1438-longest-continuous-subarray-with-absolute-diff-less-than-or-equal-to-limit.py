class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
# core concept : diff of greatest element - smallest element in window should be smaller than limit
# rest all diff would be automatically smaller
        from collections import deque

        def diff():

            s_que = deque()
            l_que = deque()
            n = len(nums)
            max_len = 0
            r = 0
            l = 0
            diff = 0

            for r in range(len(nums)):              

                while s_que and nums[s_que[-1]] > nums[r]:
                    s_que.pop()
                s_que.append(r)
            
                while l_que and nums[l_que[-1]] < nums[r]:
                    l_que.pop()
                l_que.append(r)


                #  if difference is smaller than limit, extend window size ,if greater, reduce
                
                

                while nums[l_que[0]] - nums[s_que[0]] > limit:
                    
                    if s_que and s_que[0] == l:
                        s_que.popleft()

                    if l_que and l_que[0] == l:
                        l_que.popleft()
                    
                    l += 1


                max_len = max(max_len,(r-l)+1)
                 
                    
            return max_len
        return diff()

                

                # large deque
                

                
            

                

                


