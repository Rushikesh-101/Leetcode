class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def kclose():

            hip = []
            heapq.heapify(hip)
            res = []

            for point in points:
                x,y = point
                dist = ((x**2)+(y**2))**0.5
                heapq.heappush(hip,(-dist,(point)))

                if len(hip) > k:
                    heapq.heappop(hip)
            
            while hip:
                pop = heapq.heappop(hip)
                res.append(pop[1])
            
            return res
        
        return kclose()