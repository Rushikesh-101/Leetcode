class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        def medianSlidingWidow(nums, k):
            small = []   # max heap (negative values)
            large = []   # min heap
            delayed = defaultdict(int)

            small_size = 0
            large_size = 0

            def prune(heap):
                while heap:
                    val = -heap[0] if heap is small else heap[0]
                    if delayed[val] > 0:
                        delayed[val] -= 1
                        heapq.heappop(heap)
                    else:
                        break

            def rebalance():
                nonlocal small_size, large_size
                if small_size > large_size + 1:
                    heapq.heappush(large, -heapq.heappop(small))
                    small_size -= 1
                    large_size += 1
                    prune(small)
                elif small_size < large_size:
                    heapq.heappush(small, -heapq.heappop(large))
                    large_size -= 1
                    small_size += 1
                    prune(large)

            def add(num):
                nonlocal small_size, large_size
                if not small or num <= -small[0]:
                    heapq.heappush(small, -num)
                    small_size += 1
                else:
                    heapq.heappush(large, num)
                    large_size += 1
                rebalance()

            def remove(num):
                nonlocal small_size, large_size
                delayed[num] += 1
                if num <= -small[0]:
                    small_size -= 1
                    if num == -small[0]:
                        prune(small)
                else:
                    large_size -= 1
                    if large and num == large[0]:
                        prune(large)
                rebalance()

            def get_median():
                if k % 2 == 1:
                    return float(-small[0])
                return (-small[0] + large[0]) / 2.0

            res = []

            for i in range(len(nums)):
                add(nums[i])
                if i >= k - 1:
                    res.append(get_median())
                    remove(nums[i - k + 1])

            return res
        
        return medianSlidingWidow(nums, k)