class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # (0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1) 8 directional

        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1
        
        if len(grid)==1 and len(grid[0])==1:
            if grid[0][0] == 0:
                return 1
            else:
                return -1

        steps = 1



        for x,y in [(0,1),(1,0),(1,1)]:

            if grid[x][y] == 0:
                queue.append((x,y))

            if x == rows-1 and y == cols-1:
                    return steps+1
        steps += 1

        while queue:
            
            for _ in range(len(queue)):
                x,y = queue.popleft()

                if x == rows-1 and y == cols-1:
                    return steps

                for a,b in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]:
                    nx,ny = x+a, y+b

                    if nx == rows-1 and ny == cols-1:
                        print("worked")
                        print("this is grid bfr return:",grid)
                        return steps+1
                    elif 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                        grid[nx][ny] = "T"
                
                        queue.append((nx,ny))
                    
                
            steps += 1
        
        return -1
                    
            
