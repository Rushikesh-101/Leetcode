class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        import copy

        
        
        rat = copy.deepcopy(mat)
        
        
            
               

        
        



        for r in range(rows):
            for c in range (cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
    

        ctr = 1
        while queue:      

            for _ in range(len(queue)):
                x,y = queue.popleft()


                for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+a,y+b
                
                    if 0 <= nx < rows and 0 <= ny < cols and mat[nx][ny] == 1:
                        queue.append((nx,ny))
         
                        mat[nx][ny] = 0
                        rat[nx][ny] = ctr
   
                        
            ctr += 1



        return rat
                    

