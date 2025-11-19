class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adj = {}
        for i in range(1,n+1):
            adj[i] = []

        for enemies in dislikes:
            a,b = enemies
            adj[a].append(b)
            adj[b].append(a)
        
        print("\n Printing adj list : ", adj)
        





        color = [] # is 0 indexed 

        for i in range(n):
            color.append(-1)
        
        
        queue = deque()

        for i in range(len(color)):

            if color[i] == -1:

                queue.append(i+1)
                color[i] = 0


            while queue:

                node = queue.popleft()
                
                if color[node-1] == 1:
                    opp = 0
                else:
                    opp = 1

                for neighbour in adj[node]:
                    if color[neighbour-1] == -1:
                        queue.append(neighbour)
                        color[neighbour-1] = opp
                    
                    elif color[neighbour-1] == color[node-1]:
                        return False
                
        return True   
                    



            


        

                
