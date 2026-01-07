class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp = {
        #     (len(cost)-1) : cost[len(cost)-1],
        #     (len(cost)-2) : cost[len(cost)-2]
        # }

        # def climb(step):
        #     if step > len(cost)-1:
        #         return 0
        #     if (step) in dp:
        #         return dp[(step)]

        #     else :
        #         cost_1 = climb(step+1)
        #         cost_2 = climb(step+2)
        #         dp[(step)] = min(cost_1,cost_2) + cost[step]
        #         return min(cost_1,cost_2) + cost[step]
        
        # return min(climb(0),climb(1))

        # def climb():
        #     dp = {
        #         (len(cost)-1) : cost[len(cost)-1],
        #         (len(cost)-2) : cost[len(cost)-2]
        #     }
        #     for i in range(len(cost)-3,-1,-1):
        #         cost_i = min( dp[(i+1)], dp[(i+2)] ) + cost[i]
        #         print("\n for index ",i," val saved ", min(cost[i+1],cost[i+2]), cost[i])
        #         dp[(i)] = cost_i
            
        #     print(dp)
        #     return min(dp[(0)],dp[(1)]) 

        # return climb()

        def climb():

            last_1 = 0
            last_2 = cost[0]

            for i in range(1,len(cost)):

                curr_cost = cost[i] + min(last_1,last_2)
                last_1 = last_2
                last_2 = curr_cost
            
            return min(curr_cost,last_1)
        return climb()


