class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        else:
            from collections import defaultdict

            nodeDict = defaultdict(list)
            for u,v in edges:

                nodeDict[u].append(v)
                nodeDict[v].append(u)
            
            stack = []
            visited = set()

            stack.append(source)

            while stack :
                node = stack.pop()
                
                if node not in visited:
                    visited.add(node)

                    for value in nodeDict[node]:
                        if value == destination:
                            return True
                        else :
                            if value not in visited:
                                stack.append(value)


            return False