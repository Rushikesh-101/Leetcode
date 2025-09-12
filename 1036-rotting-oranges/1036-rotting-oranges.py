class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[0][0] == 0 or grid[0][0] == 2:
                return 0
            
            elif grid[0][0] == 1:
                return -1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
        mins = -1
        while queue:

            for _ in range(len(queue)):
                print("entered")

                x,y = queue.popleft()

                for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                    nx,ny = a+x,b+y
                
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
            mins += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    return mins
         
        return 0