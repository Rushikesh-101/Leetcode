class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        DP [coins to choose from][amount remaining]
        '''
        DP = {}
        def demoni(x, amt):
           
            
            if amt == 0 :
                return 0
            if amt < 0:
                return float('inf')

            for i in range(x,len(coins)):
                if (i, amt) in DP:
                    return DP[(i, amt)]
                # not take :
                result = demoni(i+1,amt)

                if coins[i] <= amt:
                    result = min(result, demoni(x,amt-coins[i]) + 1)
                DP[(x, amt)] = result
                return result
            return float('inf')

        
        result = demoni(0, amount)
        if result == float('inf'):
            return -1
        else:
            return result