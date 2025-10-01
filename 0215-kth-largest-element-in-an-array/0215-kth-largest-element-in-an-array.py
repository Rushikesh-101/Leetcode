class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-x for x in nums]
        heapq.heapify(num)
        print("num is this : ",num)
        size = k-1
        while size :
            heapq.heappop(num)
            size -= 1
       
        return -heapq.heappop(num)