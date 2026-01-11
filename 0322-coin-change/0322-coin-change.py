class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        DP [coins to choose from][amount remaining]
        '''
        DP = {}
        def demoni(x, amt):
            if (x,amt) in DP:
                return DP[(x,amt)]

            if x == len(coins):
                return float('inf')
            if amt == 0 :
                return 0
            if amt < 0:
                return float('inf')

            

            result = demoni(x+1,amt)
            if coins[x] <= amt :
                result = min(result, demoni(x,amt-coins[x])+1)
            
            DP[(x,amt)] = result
            return result

        



        result = demoni(0, amount)
        if result == float('inf'):
            return -1
        else:
            return result














        # for i in range(x,len(coins)):
        #         if (i, amt) in DP:
        #             return DP[(i, amt)]
        #         # not take :
        #         result = demoni(i+1,amt)

        #         if coins[i] <= amt:
        #             result = min(result, demoni(x,amt-coins[i]) + 1)
        #         DP[(x, amt)] = result
        #         return result
        #     return float('inf')