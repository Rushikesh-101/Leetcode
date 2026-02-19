class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def store(mid):
            stores = 0
            for q in quantities:
                if q <= mid:
                    stores +=1
                else:
                    if q%mid == 0:
                        stores += q//mid
                    else:
                        stores += (q//mid)+1
            if stores <= n:
                return True
            else:
                return False
                

        def retailer():
            right = max(quantities)
            left = 1

            while left < right:
                mid = left + (right-left)//2

                if store(mid):
                    right = mid 
                else:
                    left = mid +1
                
                
            return right

        return retailer()