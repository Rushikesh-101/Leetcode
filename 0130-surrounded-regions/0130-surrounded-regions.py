class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        from collections import deque
        queue = deque()
        rows = len(board)
        cols = len(board[0])


        def bfs(a,b):
            queue.append((a,b))
            board[a][b] = "Y"

            while queue:

                x,y = queue.popleft()

                for xx,yy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx,ny = x+xx,y+yy

                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O":
                        board[nx][ny] = "Y"
                        queue.append((nx,ny))

                
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r,0)

            if board[r][cols-1] == "O":
                bfs(r,cols-1)

        for c in range(cols):
            if board[0][c] == "O":
                bfs(0,c)

            if board[rows-1][c] == "O":
                bfs(rows-1,c)
        print("this ")
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Y":
                    board[r][c] = "O"
        
            

           