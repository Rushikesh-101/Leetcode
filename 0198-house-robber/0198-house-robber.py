class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]


        # In DP store indexes and the max value they can provide ahead of them.
        # dp = {}
        # def maxi(i):
        #     if i in dp:
        #         return dp[i]
        #     if i+2 > len(nums)-1 :
        #         dp[i] = nums[i]
        #         return nums[i]
            
        #     else:
        #         grtst = 0
        #         for idx in range(i+2,len(nums)):
        #             sum = 0
        #             sum += maxi(idx)
        #             if sum > grtst:
        #                 grtst = sum

        #         result = grtst + nums[i]
        #         dp[i] = result
        #         print("\n result for idx",i,"is :",result)
        #         return result

        # return max(maxi(0),maxi(1))

        if len(nums) < 3:
            if len(nums) == 2 :
                return max(nums[0],nums[1])
            else:
                return nums[0]

        def rob():
            last_1 = max(nums[0],nums[1])
            last_2 = nums[0]

            for i in range(2, len(nums)):
                curr_val = max(nums[i]+last_2, last_1)
                last_2 = last_1
                last_1 = curr_val

            return curr_val
        
        return rob()


