class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # all values are positive

        # so to form max heap using heapify( it creates minheap ) : we negate all values

        # then use while loop 
            #compare : choose larger, substract, push to stones

        
        for index,values  in enumerate(stones):

            stones[index] = -values
        
        print("Check if it was negate : ", stones)

        heapq.heapify(stones)

        while stones :

            stone1 = heapq.heappop(stones)
            if stones:
                stone2 = heapq.heappop(stones) 
            else :
                return -stone1

            if stone1 < stone2 :
                val = stone1 - stone2
                heapq.heappush(stones,val)
            elif stone1 > stone2 :
                val = stone2 - stone1
                heapq.heappush(stones,val) 
            else :
                print("Both were destroyed ")
        
        return 0

                