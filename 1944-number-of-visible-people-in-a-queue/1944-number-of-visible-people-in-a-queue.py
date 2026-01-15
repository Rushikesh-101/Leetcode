class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        my_vision = [0]*len(heights)
        mono = []
        for i in range(len(heights)-1, -1, -1):
            blocks = 0
            while mono and heights[mono[-1]] <= heights[i]:
                pop = mono.pop()
                blocks += 1
            if mono:
                my_vision[i] = blocks+1
            else:
                my_vision[i] = blocks
            
            mono.append(i)
            
        return my_vision


