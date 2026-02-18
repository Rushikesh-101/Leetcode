class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def bouquets(mid):
            adj = k
            count = m
            for f in bloomDay:
                if f <= mid:
                    adj -= 1
                else:
                    adj = k

                if adj == 0:
                    count -= 1
                    adj = k
            if count <= 0:
                return True
            else:
                return False
        def make_bouquets():
            left = float('inf')
            right = 0
            for f in bloomDay:
                left = min(left,f)
                right = max(right,f)
            
            while left < right:
                mid = left + (right-left)//2

                if bouquets(mid):
                    right = mid
                else:
                    left = mid+1

            mid = left + (right-left)//2

            if bouquets(mid):
                right = mid
            else:
                return -1
            
            return mid
        
        return make_bouquets()




                