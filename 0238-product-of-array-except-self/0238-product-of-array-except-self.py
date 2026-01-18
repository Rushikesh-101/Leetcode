class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        answer = [1]*n
        
        for i in range(1,n):
            answer[i] = answer[i-1]*nums[i-1]
            print(i,answer[i])
        
        suffix = 1
        for i in range(n-2,-1,-1):
            suffix = suffix*nums[i+1]
            answer[i] = suffix*answer[i]

       
        return answer 

        '''
        Mistakes I made above :
        - used 2 prefix suffix arrays - you only need 1 answer array
        - update prefix in answer array - then use a variable to update
          suffix values in same answer array

        - I used 2 patch works for edge cases

        '''

