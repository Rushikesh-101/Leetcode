class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        def bad_description():
            print(len(costs))
            l = -1 
            r = len(costs)
            hip = []
            heapq.heapify(hip)
            total_cost = 0
            mid = r//2

            for _ in range(candidates):
                l+=1
                r-=1
                if l < r: 
                    heapq.heappush(hip,(costs[l],l))
                    heapq.heappush(hip,(costs[r],r))
                elif l == r:
                    heapq.heappush(hip,(costs[l],l))
            
            print(len(hip))
            

            for _ in range(k):
                pop = heapq.heappop(hip)
                
                total_cost += pop[0]

                # next element from either half
                if l < r and r-1 != l:
                    
                    if pop[1] >= r: # next element should be taken from right half
                        r -= 1
                        heapq.heappush(hip,(costs[r],r))

                    elif pop[1] <= l:
                        l += 1
                        heapq.heappush(hip,(costs[l],l))
            
            return total_cost
        
        return bad_description()


