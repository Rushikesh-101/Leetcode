class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        '''
        Had problem in clearly understanding the question:
        Have to return tha min capability means
        Minimum capability means : out of all sets possible we leave him with least value set
        But out of all values in that set he will choose max possible robbery
        '''

        '''
        So approach is to find a min cap integer for k set of non adjacent digits smaller or equal to it in array
        This min cap would be the min capability you can return cause its one of the least possible value set, and its max of that set.
        '''
        def house(mid):
            ctr = 0
            count = 0
            for n in nums:
                if n <= mid and ctr == 0:
                    
                    ctr = 1
                    count += 1
                else:
                    ctr = 0
            if count >= k:
                return True
            else:
                return False


        def robber():

            left = min(nums)
            right = max(nums)

            while left < right:
                mid = left + (right-left)//2   

                if house(mid):
                    right = mid
                else:
                    left = mid+1
            
            return right
        
        return robber()