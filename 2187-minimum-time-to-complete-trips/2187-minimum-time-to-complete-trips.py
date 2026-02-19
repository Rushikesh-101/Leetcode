class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def trip(mid):
            print(mid)
            count = 0
            for t in time:
                if t <= mid:
                    count += mid//t
            
            if count >= totalTrips:
                return True
            else:
                return False


        def buses():
            right = min(time)*totalTrips
            left = 1

            while left < right:
                mid = left + (right-left)//2

                if trip(mid):
                    right = mid
                else:
                    left = mid+1

            return right
        
        return buses()
            