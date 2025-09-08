class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        global Area 
        Area = 0
        global maxArea 
        maxArea = 0

        def bfs(a,b):
            queue.append((a,b))
            grid[a][b] = 0
            global Area
            Area += 1
            

            while queue:
                aa,bb = queue.popleft()
                for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = aa+x,bb+y

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        Area += 1
                        queue.append((nx,ny))
    
        if not grid:
            return 0

        else:

            for r in range(rows):
                for c in range(cols):
                    
                    if grid[r][c] == 1:
                        bfs(r,c)
                    if maxArea < Area :
                        maxArea = Area
                    Area = 0

            return maxArea