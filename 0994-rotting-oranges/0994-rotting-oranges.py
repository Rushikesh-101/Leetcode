class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        def oranges():
            que = deque()
            rows = len(grid)
            cols = len(grid[0])
            visited = set()
            neigh = ((0,1),(1,0),(-1,0),(0,-1))
            # Fill que with initial rots
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        que.append((r,c))
            
            min = 0
            while que:
                for i in range(len(que)):
                    r,c = que.popleft()
                    for a,b in neigh:
                        nrow = a+r
                        ncol = b+c
                        if (nrow,ncol) in visited:
                            pass
                        elif 0 <= nrow < rows and 0 <= ncol < cols:
                            if grid[nrow][ncol] == 1:
                                grid[nrow][ncol] = 2
                                visited.add((nrow,ncol))
                                que.append((nrow,ncol))
                            else:
                                pass
                min += 1
            
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        return -1
            if min:
                return min-1
            else:
                return 0

        return oranges()


