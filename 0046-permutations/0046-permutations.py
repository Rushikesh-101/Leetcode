class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        nums = set(nums)
        result = []

        def recur(nums, array):
            nonlocal result
            if len(nums) == 0:
                result.append(array)
            
            else:
                for i in nums.copy():
                    array.append(i)
                    nums.remove(i)
                    recur(nums, array[:])
                    nums.add(i)
                    array.pop()

        array = []
        recur(nums, array)
        return result

                
