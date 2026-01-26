class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def short():
            que = deque()
            temp_que = deque()
            rows = len(grid)
            cols = len(grid[0])
            neigh = ((0,1),(1,0),(0,-1),(-1,0))
            found = 0
            
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        grid[r][c] = -1
                        que.append((r,c))
                        temp_que.append((r,c))
                        found = 1
                        break
                if found == 1:
                    break

            # All blocks of one island filled up into a que for start
            while temp_que:
                r,c = temp_que.popleft()
                for a,b in neigh:
                    nrow = a+r
                    ncol = b+c
                    if 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = -1
                        temp_que.append((nrow,ncol))
                        que.append((nrow,ncol))
            
            flips = 0
            while que:
                for i in range(len(que)):
                    r,c = que.popleft()
                    for a,b in neigh:
                        nrow = a+r
                        ncol = b+c
                        if 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == 1:
                            print(nrow,ncol)
                            return flips
                        elif 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == 0:
                            grid[nrow][ncol] = -1
                            que.append((nrow,ncol))
                flips += 1

        return short()



            
