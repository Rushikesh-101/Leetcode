class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        base = image[sr][sc]
        from collections import deque
        queue = deque()
        rows = len(image)
        cols = len(image[0])


        def bfs(a,b):

            queue.append((a,b))
            image[a][b] = color

            while queue:
                
                x,y = queue.popleft()
                

                for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:

                    nx,ny = a+x,b+y

                    if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == base:
                        image[nx][ny] = color
                        queue.append((nx,ny))


        if color == base:
            return image       
        
        bfs(sr,sc)

        return image

