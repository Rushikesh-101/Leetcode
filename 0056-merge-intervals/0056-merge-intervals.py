class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def merge_overlaps():

            res = []
            intervals.sort(key = lambda x : x[1])
            res.append(intervals[0])

            for i in range(1,len(intervals)):
                if (intervals[i][0]) <= (res[-1][1]):
                    while res and (intervals[i][0]) <= (res[-1][1]):
                        pop = res.pop()
                    if pop[0] < intervals[i][0]:
                        new = [pop[0],intervals[i][1]]
                    else:
                        new = intervals[i]
                    res.append(new)
                else:
                    res.append(intervals[i])
                
            return res


        return merge_overlaps()