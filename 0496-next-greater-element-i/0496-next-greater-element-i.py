class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # go through nums 2 , map the nge in a dict with the respective values
        # go through nums 1, check each i as key in dict , if there , use its value in return array
        # at end return result array

        def nxt_gen_ele():
            hash_map = {}
            mono = []

            for i in range(len(nums2)):
                if not mono:
                    mono.append(i)
                else:
                    while mono and nums2[mono[-1]] < nums2[i]:
                        pop = mono.pop()
                        hash_map[nums2[pop]] = nums2[i]
                    mono.append(i)
            while mono :
                pop = mono.pop()
                hash_map[nums2[pop]] = -1
            
            result = []
            for val in nums1:
                result.append(hash_map[val])
            return result
        
        return nxt_gen_ele()





