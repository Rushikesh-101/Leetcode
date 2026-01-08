class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        DP = {}
        for i in nums :
            if i in DP:
                DP[i] += i
            else:
                DP[i] = i
        
        max_val = max(DP)

        last_2 = 0
        last_1 = 0
        print(max_val)
        
        for i in range(1,max_val+1):
            if i in DP:
                curr_val = max(DP[i]+last_2 , last_1)
                last_2 = last_1
                last_1 = curr_val
            else:
                curr_val = max(last_2 , last_1)
                last_2 = last_1
                last_1 = curr_val
        return last_1
        
       
        

             

            

