class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        '''
        -intuition : maintain 2 stack , 1 monotonic, another reserve.
        - elements popped from mono are pushed into reserve stack
        - next traversed element first looks into reserved stack, empties any smaller element in it 
        - PROBLEM ! : top of reserve could be bigger than current but below that might be smaller, so we maintain an array

        - problem FIX : use midle man temp stack to maintain the order
        
        '''

        def second_smaller():
            mono = []
            second = []
            result = [-1]*len(nums)
            for i in range(len(nums)):
                while second and nums[second[-1]] <  nums[i]:
                    second_pop = second.pop()
                    result[second_pop] = nums[i]

                temp = []
                while mono and nums[mono[-1]] < nums[i]:
                    temp.append(mono.pop())
                mono.append(i)
                while temp:
                    second.append(temp.pop())
            return result 
        
        return second_smaller()

        # YAYYYY ! 