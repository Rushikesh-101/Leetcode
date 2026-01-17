class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        '''
        - same as ctr and element technique of  n/2 majority problem.
        - only use 2 elements and 2 ctrs  
        '''


        def maj_of_2():
            ele_1 = None
            ele_2 = None
            ctr_1 = 0
            ctr_2 = 0

            for i in nums:

                if ctr_1 == 0 and ele_2 != i:
                    ele_1 = i
                    ctr_1 = 1
                elif ctr_2 == 0 and ele_1 != i:
                    ele_2 = i
                    ctr_2 = 1
                
                elif ele_1 == i:
                    ctr_1 += 1
                elif  ele_2 == i:
                    ctr_2 += 1
                
                else:
                    ctr_1 -= 1
                    ctr_2 -= 1

            # Youve to verify the majority for ele 1 and ele 2 manually too cause counter dont represent actual frequency

            res = []
            n = len(nums)

            ctr_1 = ctr_2 =0
            for i in nums:
                if i == ele_1:
                    ctr_1 += 1
                elif i == ele_2:
                    ctr_2 += 1
            if ctr_1 > n/3:
                res.append(ele_1)
            if ctr_2 > n/3:
                res.append(ele_2)
        
            return res
        
        return maj_of_2()