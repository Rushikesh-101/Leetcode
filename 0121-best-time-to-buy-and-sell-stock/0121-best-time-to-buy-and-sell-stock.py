class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def SellNow():
            smallest = prices[0]
            maxi = 0

            for val in prices:

                if val < smallest:
                    smallest = val

                diff = val - smallest
                if diff > maxi:
                    maxi = diff

            return maxi

        return SellNow()