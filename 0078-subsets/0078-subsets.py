class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def numberOfSubsets():
            size = len(nums)
            res_list = []
            for sett in range(0,2**size):
                temp_list = []
                for j in range(0,size):
                    if sett & (1 << j):
                        temp_list.append(nums[j])
                res_list.append(temp_list)
            return res_list
        
        return numberOfSubsets()
