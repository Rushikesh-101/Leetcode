class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp = {
        #     str(len(cost)-1) : cost[len(cost)-1],
        #     str(len(cost)-2) : cost[len(cost)-2]
        # }

        # def climb(step):
        #     if step > len(cost)-1:
        #         return 0
        #     if str(step) in dp:
        #         return dp[str(step)]

        #     else :
        #         cost_1 = climb(step+1)
        #         cost_2 = climb(step+2)
        #         dp[str(step)] = min(cost_1,cost_2) + cost[step]
        #         return min(cost_1,cost_2) + cost[step]
        
        # return min(climb(0),climb(1))
        def climb():
            dp = {
                str(len(cost)-1) : cost[len(cost)-1],
                str(len(cost)-2) : cost[len(cost)-2]
            }
            for i in range(len(cost)-3,-1,-1):
                cost_i = min( dp[str(i+1)], dp[str(i+2)] ) + cost[i]
                print("\n for index ",i," val saved ", min(cost[i+1],cost[i+2]), cost[i])
                dp[str(i)] = cost_i
            
            print(dp)
            return min(dp[str(0)],dp[str(1)]) 

        return climb()