class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        here we run house robber 1 algo on 2 ranges :
        1 without first element 
        1 without last element
        '''

        if len(nums) < 4:
            lenght = len(nums)
            if lenght == 3 :
                return max(nums[0],nums[1],nums[2])
            elif lenght == 2 :
                return max(nums[0],nums[1])
            else:
                return nums[0]

        def climb(x,y):
            last_2 = nums[x]
            last_1 = max(nums[x+1],nums[x])

            curr_val = 0
            for i in range(x+2,y+1):
                curr_val = max(nums[i]+last_2, last_1)
                last_2 = last_1
                last_1 = curr_val
            return curr_val
        
        with_first = climb(0,len(nums)-2)
        with_last = climb(1,len(nums)-1)

        return max(with_first,with_last)

                

            