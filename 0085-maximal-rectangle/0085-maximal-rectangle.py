class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        '''
        updating height and then performing histogram functions at each row 
        '''
        
        
        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for r in range(rows):     
            mono = []
            for c in range(cols):
                if matrix[r][c] == '0' : 
                    heights[c] = 0
                else :
                    heights[c] += 1

            for i in range(len(heights)):
                while mono and int(heights[mono[-1]]) >= int(heights[i]):
                    area = 0
                    k = mono.pop()
                    L = mono[-1] if mono else -1
                    R = i
                    area = heights[k] * (R - L -1)
                    max_area = max(max_area,area)
                mono.append(i)

            while mono :
                area = 0
                k = mono.pop()
                L = mono[-1] if mono else -1
                R = cols
                area = heights[k] * (R- L - 1)
                max_area = max(max_area,area)
                
        return max_area
            

                
             


