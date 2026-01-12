class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        DP [coins to choose from][amount remaining]
        '''
        # DP = {}
        # def demoni(x, amt):
        #     if (x,amt) in DP:
        #         return DP[(x,amt)]

        #     if x == len(coins):
        #         return float('inf')
        #     if amt == 0 :
        #         return 0
        #     if amt < 0:
        #         return float('inf')

            

        #     result = demoni(x+1,amt)
        #     if coins[x] <= amt :
        #         result = min(result, demoni(x,amt-coins[x])+1)
            
        #     DP[(x,amt)] = result
        #     return result

        



        # result = demoni(0, amount)
        # if result == float('inf'):
        #     return -1
        # else:
        #     return result






        # OPTIMAL SOLUTION with 1D DP
        # BOTTOM UP APPROACH
        # we build DP[0] TO DP[amount]

        def opt_coins():
            DP = [float('inf')] * (amount+1)
            DP[0] = 0
            for x in range(0,amount+1):
                for coin in coins:
                    if coin <= x :
                        DP[x] = min(DP[x], DP[x-coin] + 1)
                    
            if DP[amount] == float('inf'):
                return -1
            else :
                return DP[amount]
        
        return opt_coins()



            



