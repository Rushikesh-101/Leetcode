class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        queue = deque()  
        colorArray = []

        # creating color array
        for i in range(len(graph)):
            colorArray.append(-1)

        for i in range(len(colorArray)):
            
            # to ensure no colorArray index remains uncolored
            if colorArray[i] == -1:

                queue.append(i)
                colorArray[i] = 0

            # pop queue check neighbors for opposite color, if not color add to queue
            while queue:

                node = queue.popleft()
                opp = 0
                if colorArray[node] == 0:
                    opp = 1
                else: 
                    opp = 0

                for neighbours in graph[node]:
                    if colorArray[neighbours] == -1 :
                        colorArray[neighbours] = opp
                        queue.append(neighbours)
                    
                    elif colorArray[neighbours] == colorArray[node] :
                        return False

        return True

                