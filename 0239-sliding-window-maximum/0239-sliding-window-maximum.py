class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # track index range using k

        # traverse nums using for
            #once at end of curr window : calc max( ie the front element in que)
        que = deque()
        front = 0
        rear = 0
        a = 0
        b = 2
        res = []
        ctr = 0
        itr = 0
        for index in range(len(nums)):
            ctr += 1

            # this pops indexes from que that are out of current window
            while que and que[0] < a:
                que.popleft()

            if not que:
                que.append(index)
            else:
                while que and nums[index] > nums[que[-1]]:
                    que.pop()
                que.append(index)
            


            
            if ctr >= k:
                res.append(nums[que[0]])

            if ctr >= k:
                a +=1
                b +=1


            
            
                

        return res
                
            



        #initiate deque with F = 0 and rear = -1

        # if que empty direct at rear

        # for next elements compare with rear. 
            # while grt than rear. pop rear

        # when calc max : while front is out of window. pop front


        
        