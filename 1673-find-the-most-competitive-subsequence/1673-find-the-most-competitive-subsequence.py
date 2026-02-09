class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
        def competition(k):
            stack = []
            size = len(nums)
            for i in range(len(nums)):
                if len(stack) == k:
                    if stack[-1] > nums[i]:
                        while stack and (k-len(stack)) < (size-i) and stack[-1] > nums[i]:
                            stack.pop()
                        stack.append(nums[i])
                    else:
                        continue
                else:
                    while stack and (k-len(stack)) < (size-i) and stack[-1] > nums[i]:
                        stack.pop()
                    stack.append(nums[i])
            
            return stack
        
        return competition(k)
