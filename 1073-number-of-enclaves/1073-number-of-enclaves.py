class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        # If row == 0 or col == 0 its on edge
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        def bfs(a,b):
            grid[a][b] = 0
            queue.append((a,b))
            while queue:

                x,y = queue.popleft()

                for xx,yy in [(0,1),(0,-1),(1,0),(-1,0)]:

                    nx,ny = xx+x,yy+y

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        queue.append((nx,ny))
                        grid[nx][ny] = 0
            
        

        for r in range(rows):
            if grid[r][0] == 1:
                bfs(r,0)
            if grid[r][cols-1] == 1:
                bfs(r,cols-1)
        for c in range(cols):
            if grid[0][c] == 1:
                bfs(0,c)
            if grid[rows-1][c] == 1:
                bfs(rows-1,c)
        
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1

        return count 


