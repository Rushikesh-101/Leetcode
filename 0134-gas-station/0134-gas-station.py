class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        # Particular problem type :
        - Complete or traverse cycle of array based on resources
        provided.
        - Solution : 
        - Check if valid solution exist by subtracting cost from
        resource
        - Create prefix sums from index 0 
        - cycle exists from next index to smallest prefix sum 
        '''

        tot_gas = 0
        tot_cost = 0
        prefix = 0
        min_prefix = (float('inf'),0)
        for i in range(len(gas)):
            tot_gas += gas[i]
            tot_cost += cost[i]

            prefix = (gas[i]-cost[i])+prefix
            if prefix < min_prefix[0]:
                min_prefix = (prefix,i)
        if tot_gas-tot_cost >= 0:
            return min_prefix[1]+1 if min_prefix[1] != len(gas)-1 else 0
        else:
            return -1



                

