class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    
    # Storing frequency in a dict --- O(n)
        count = {}

        for value in nums :

            if value in count:
                count[value] += 1
            else:
                count[value] = 1
            
        print("\n this is freq dict : ", count)

    # Creating priority heap from dict keys and values --- O(n)

        freqHeap = []
        for key, value in count.items() :
            heapq.heappush(freqHeap,(value,key))
            if len(freqHeap) > k :
                heapq.heappop(freqHeap)
        print("\n Top k freq elements left in heap : ", freqHeap)
        
    # Append freqHeap tasks into res array
        res = []
        while freqHeap: 
             priority, val = heapq.heappop(freqHeap)
             res.append(val)
        
        return res