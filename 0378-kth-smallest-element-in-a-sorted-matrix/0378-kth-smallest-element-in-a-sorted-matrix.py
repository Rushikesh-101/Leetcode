class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # Note that it is the kth smallest element in the sorted order, not the kth distinct element.
        # Above means you can add duplicates
        rows = len(matrix)
        cols = len(matrix[0])
        que = deque()
        hip = []
        heapq.heapify(hip)
        que.append((0,0))
        visited = set()
        visited.add((0,0))
        neigh = ((0,1),(1,0))
        for j in range(k):
            for i in range(len(que)):
                x,y = que.popleft()
                heapq.heappush(hip,(-matrix[x][y],(x,y)))
                for a,b in neigh:
                    nx = a+x
                    ny = b+y

                    if 0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited:
                        que.append((nx,ny))
                        visited.add((nx,ny))
            while len(hip)>k:
                heapq.heappop(hip)
        pop = heapq.heappop(hip)
        return -pop[0]
    


