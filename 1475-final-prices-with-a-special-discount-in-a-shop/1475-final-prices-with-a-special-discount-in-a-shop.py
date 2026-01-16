class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        def discount():
            result = [0]*len(prices)
            mono = []
            for i in range(len(prices)):
                while mono and prices[mono[-1]] >= prices[i]:
                    k = mono.pop()
                    result[k] = prices[k] - prices[i]
                mono.append(i)
            
            while mono:
                k = mono.pop()
                result[k] = prices[k]

            return result
        
        return discount()
                