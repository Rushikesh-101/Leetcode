class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        global noIslands
        noIslands = 0

        def dfs(a,b):
            print("entered dfs")
            
            grid[a][b] = '0' #marked visited
            queue.append((a,b))

            while queue:
                x,y = queue.popleft()
                for xx,yy in [(0,1),(0,-1),(1,0),(-1,0)]:

                    nx,ny = xx+x, yy+y

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        queue.append((nx,ny))
                        grid[nx][ny] = '0'


        if not grid :
            return 0

        else :
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '1':
                        dfs(r,c)
                        noIslands += 1


            return noIslands