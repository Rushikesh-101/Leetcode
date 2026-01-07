class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        
        def climb():
            last_2 = 0
            last_1 = 0

            for i in range(2,len(cost)+1):
                curr_cost = min((cost[i-1])+ last_1, (cost[i-2])+last_2)
                last_2 = last_1
                last_1 = curr_cost
            
            return curr_cost
        return climb()
                

