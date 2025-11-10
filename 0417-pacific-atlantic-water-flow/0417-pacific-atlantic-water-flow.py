class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
    
            # For pacific ocean : check all 4 directions 

        rows = len(heights)
        cols = len(heights[0])
        setPacific = set()
        setAtlantic = set()
        visited = set()


        stack = []
        # Appending top and left edges to stack
        for c in range (cols) :
            stack.append((0,c))
        
        for r in range (rows):
            stack.append((r,0))
            

        

        while stack:
            cell = stack.pop()
            setPacific.add(cell)
        
                
            if cell not in visited :
                visited.add(cell)
                r,c = cell
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    
                    rr,cc = r+x,c+y
                    if 0<=rr<rows and 0<=cc<cols  and heights[rr][cc] >= heights[r][c]:# valid for pacific
       
                        stack.append((rr,cc))
                        


        stack = []
        visited.clear()
        # Appending top and left edges to stack
        for c in range (cols) :
            stack.append((rows-1,c))
        
        for r in range (rows):
            stack.append((r,cols-1))

        while stack:
            cell = stack.pop()
            setAtlantic.add(cell)
            
                
            if cell not in visited :
                visited.add(cell)
                r,c = cell
                for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                    
                    rr,cc = r+x,c+y
                    if 0<=rr<rows and 0<=cc<cols and (rr,cc) not in visited and heights[rr][cc] >= heights[r][c]:# valid for pacific
                    
                        stack.append((rr,cc))
                        

     
        result = []
   

        for i in setPacific.intersection(setAtlantic):
            result.append(i)
        return result
            



                





                    