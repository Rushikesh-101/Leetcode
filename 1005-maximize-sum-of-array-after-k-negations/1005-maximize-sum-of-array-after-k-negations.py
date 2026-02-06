class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        def signChange(k):

            total = 0
            nums.sort()
            print(nums)
            for i in range(len(nums)):
                if nums[i] < 0 and k > 0:
                    total += -(nums[i])
                    k -= 1
                    if i == len(nums)-1 and k > 0 and k%2 != 0:
                        total -= -(2*nums[i])
                
                elif nums[i] > 0 and k > 0:
                    if k%2 == 0:
                        total += nums[i]
                        k = 0
                    else:
                        if i != 0 and nums[i] > -(nums[i-1]):
                            total += nums[i]
                            total -= (-nums[i-1])*2
                        else:
                            total -= nums[i]
                        k = 0
                else :
                    total += nums[i]
            
            return total
        
        return signChange(k)
                        