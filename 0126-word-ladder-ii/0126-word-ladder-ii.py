class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        

        def finder():

            parent = {}
            que = deque()
            wordset = set()
            for i in wordList:
                wordset.add(i)
            visited = set()
            if endWord not in wordset:
                return []
            que.append(beginWord)
            visited.add(beginWord)

            # BFS Part
            found = 0
            while que:
                
                level_vis = set()
                if found == 1:
                    break 
                for _ in range(len(que)):
                    word = que.popleft()

                    for s in range(len(word)):
                        for a in 'abcdefghijklmnopqrstuvwxyz':
                            if word[s] == a:
                                continue
                            else:
                                new = word[:s] + a + word[s+1:]

                                if new in visited:
                                    continue
                                if new in wordset:

                                    if new not in level_vis:
                                        level_vis.add(new)
                                        que.append(new)
                                    
                                    if new not in parent:
                                        parent[new] = []
                                    parent[new].append(word)

                                    if new == endWord:
                                        found = 1

                               
                visited |= level_vis    # Union of both sets

            # DFS Part
            # This uses recursive calls to create different path, if paths new word is begin word, we save a shallow copy. 
            result = []
            path = []

            def dfs(word):
                path.append(word)
                if path[-1] == beginWord:
                    result.append(path[::-1])
                else:
                    for par in parent[word]:
                        dfs(par)
                path.pop()
            if endWord not in parent:
                return []
            dfs(endWord)
            return result
        
        return finder()



