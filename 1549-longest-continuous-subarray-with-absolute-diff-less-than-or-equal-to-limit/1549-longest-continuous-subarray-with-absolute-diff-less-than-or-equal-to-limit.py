class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        left = 0
        right = 1
        minque = deque()
        maxque = deque()
        res = []
        minque.append(left)
        maxque.append(left)
        while left <= len(nums)-2 and right <= len(nums)-1 : 
            print("\n Stuck")
            # TO DO !!!   add left and right updates after each action
            
            # queleft within window checked
            if minque and minque[0] < left :
                minque.popleft()
            if maxque and maxque[0] < left :
                maxque.popleft()


            # pushing into min and max queue by comparing
            
            while minque and nums[minque[-1]] > nums[right]:
                minque.pop()

            if not minque :
                minque.append(right)
            elif minque[-1] != right:
                minque.append(right)
            
            
            while maxque and nums[maxque[-1]] < nums[right]:
                maxque.pop()

            if not maxque :
                maxque.append(right)
            elif maxque[-1] != right :
                maxque.append(right)

            # differences of min and max of window

            if nums[maxque[0]] - nums[minque[0]] <= limit:
                res.append((left,right))
                right += 1
            
            else:
                
                if left != right - 1:
                    left += 1
                else:
                    right += 1
                    left += 1
                    

        maxVal = 0
        while res:
            x,y = res.pop()
            if y-x > maxVal:
                maxVal = (y-x)
        
        maxVal += 1
        
        return maxVal




