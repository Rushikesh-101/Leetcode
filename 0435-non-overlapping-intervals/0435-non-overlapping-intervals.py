class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        def overlapping():
            skip = 0
            intervals.sort(key = lambda x : x[1])
            clear = 0

            for i in range(1,len(intervals)):

                if intervals[i][0] < intervals[clear][1]:
                    skip += 1
                else:
                    clear = i
                    pass
            return skip
        
        return overlapping()