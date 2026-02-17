class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        BS on answer 
        min_cap = max of array
        max_cap = total of array
        '''
        def match(mid):
            
            count = 0
            cap = 0
            for w in weights:
                if cap + w <= mid:
                    cap += w
                else:
                    count += 1
                    cap = w
            count += 1
            if count <= days:
                return True
            else:
                return False


        def shipping():
            l = 0
            r = 0
            for w in weights:
                if w > l:
                    l = w
                r += w

            min_weight = float('inf')
            while l < r:
                mid = l + (r-l)//2
                
                if match(mid):
                    min_weight = min(min_weight,mid)
                    r = mid
                
                else:
                    l = mid+1
            if l == r :
                mid = l + (r-l)//2
                
                if match(mid):
                    min_weight = min(min_weight,mid)
                    r = mid
                
                else:
                    l = mid+1

            return min_weight 
        
        return shipping()



        
