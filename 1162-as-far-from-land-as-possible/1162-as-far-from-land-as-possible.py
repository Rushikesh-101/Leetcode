class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        

        def afar():
            rows = len(grid)
            cols = len(grid[0])
            que = deque()
            neigh = ((0,1),(1,0),(0,-1),(-1,0))
            max_dist = 0
            for r in range(rows):
                for c in range (cols):
                    if grid[r][c] == 1:
                        que.append((r,c))
            if not que:
                return -1

            while que:
                ctr = 0
                for _ in range(len(que)):
                    r,c = que.popleft()
                    for a,b in neigh:
                        nrow = a+r
                        ncol = b+c
                        if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == 0:
                            grid[nrow][ncol] = 1
                            que.append((nrow,ncol))
                            ctr = 1
                if ctr == 1:
                    max_dist += 1
            if not max_dist:
                return -1        
            return max_dist
        return afar()
        
                    