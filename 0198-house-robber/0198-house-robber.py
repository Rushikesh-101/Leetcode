class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

            
        # In DP store indexes and the max value they can provide ahead of them.
        dp = {}
        def maxi(i):
            if i in dp:
                return dp[i]
            if i+2 > len(nums)-1 :
                dp[i] = nums[i]
                print("\n result for idx",i,"is :",nums[i])
                return nums[i]
            
            else:
                grtst = 0
                for idx in range(i+2,len(nums)):
                    sum = 0
                    sum += maxi(idx)
                    if sum > grtst:
                        grtst = sum

                result = grtst + nums[i]
                dp[i] = result
                print("\n result for idx",i,"is :",result)
                return result

        return max(maxi(0),maxi(1))

