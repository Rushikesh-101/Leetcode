class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        def height():
            rows = len(isWater)
            cols = len(isWater[0])
            neigh = ((0,1),(1,0),(-1,0),(0,-1))
            que = deque()
            for r in range(rows):
                for c in range(cols):
                    if isWater[r][c] == 1:
                        isWater[r][c] = 0
                        que.append((r,c))
                    else:
                        isWater[r][c] = -1 
            while que:               
                r,c = que.popleft()
                for a,b in neigh:
                    nrow = r+a
                    ncol = c+b

                    if 0<=nrow<rows and 0<=ncol<cols and isWater[nrow][ncol] == -1 :
                        isWater[nrow][ncol] = isWater[r][c]+1
                        que.append((nrow,ncol))
            
            return isWater
        
        return height()
                
        # In above code set usage is unnecessary, can assign -1 to lands in first parsing.
            
