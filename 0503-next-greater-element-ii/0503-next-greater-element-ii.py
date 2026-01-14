class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        def NGE2():
            result = []
            for i in range(len(nums)):
                result.append(-1)

            mono = []

            for i in range (len(nums)):
                if not mono:
                    mono.append(i)

                else :
                    while mono and nums[mono[-1]] < nums[i]:
                        popped = mono.pop()
                        result[popped] = nums[i]
                    mono.append(i)
                
            if mono:
                for i in range (len(nums)):
                    if not mono:
                        mono.append(i)

                    else :
                        while mono and nums[mono[-1]] < nums[i]:
                            popped = mono.pop()
                            result[popped] = nums[i]
                        mono.append(i)

            return result

        return NGE2()



