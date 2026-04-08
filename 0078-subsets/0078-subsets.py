class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def recurse(i,stack):
            nonlocal result
            if i > len(nums)-1:
                return
            
            else:
                recurse(i+1,stack[:])    # not taking i'th element
                stack.append(nums[i])
                result.append(stack[:])
                recurse(i+1,stack[:])    # taking i'th elment
        
        stack = []
        recurse(0,stack)

        return result
