class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        myHeap = []

        for a,b in points :
            val = math.sqrt(a*a + b*b)
            heapq.heappush(myHeap,(val,(a,b)))
        size = k
        print(myHeap)

        res = []
        while size > 0:
            val = heapq.heappop(myHeap)
            res.append(val[1])

            size -= 1
        

        return res

