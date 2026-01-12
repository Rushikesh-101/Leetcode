class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        DP = {}
        def target_sum(x,tgt):
            if (x,tgt) in DP:
                return DP[(x,tgt)]

            if x == len(nums) :
                if tgt == 0:
                    DP[(x,tgt)] = 1
                    return 1
                else:
                    DP[(x,tgt)] = 0
                    return 0

            
            
            # not taking x index num :
            result = target_sum(x+1, tgt-nums[x]) + target_sum(x+1, tgt+nums[x])

            DP[(x,tgt)] = result
            return result


            
        return target_sum(0,target)
            
