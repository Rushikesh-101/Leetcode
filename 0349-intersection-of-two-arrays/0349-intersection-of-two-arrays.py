class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        common = set()
        array = set()
        for i in nums1:
            common.add(i)
        for i in nums2:
            if i in common:
                array.add(i)

        

            

        return list(array)