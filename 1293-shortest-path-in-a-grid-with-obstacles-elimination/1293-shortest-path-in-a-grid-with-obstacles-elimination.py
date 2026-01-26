class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        def shawty_path(k):
            rows = len(grid)
            cols = len(grid[0])
            if rows == 1 and cols == 1:
                return 0
            que = deque()
            neigh = ((0,1),(1,0),(-1,0),(0,-1))
            visited = set()
            que.append(((0,0),k))
            visited.add(((0,0),k))


            path = 1
            while que:
                for i in range(len(que)):
                    (r,c),k = que.popleft()
                    for a,b in neigh:
                        nrow = r+a
                        ncol = c+b

                        if nrow == rows-1 and ncol == cols-1:
                            return path
                        elif 0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == 0:
                            if ((nrow,ncol),k) not in visited:
                                que.append(((nrow,ncol),k))
                                visited.add(((nrow,ncol),k))
                        elif  0<=nrow<rows and 0<=ncol<cols and grid[nrow][ncol] == 1 and k>0:
                            if ((nrow,ncol),k-1) not in visited:
                                que.append(((nrow,ncol),k-1))
                                visited.add(((nrow,ncol),k-1))
                path += 1
            return -1
        return shawty_path(k)   


