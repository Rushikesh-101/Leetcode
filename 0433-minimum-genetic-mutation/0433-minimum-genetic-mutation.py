class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        def gene():

            que = deque()
            geneset = set()
            choice = 'ACGT'

            for i in bank:
                geneset.add(i)
            que.append(startGene)

            if startGene in geneset:
                geneset.remove(startGene)
            
            

            count = 1
            while que:
                for _ in range(len(que)):
                    word = que.popleft()
                    for s in range(len(word)):
                        for c in choice:
                            new = word[:s] + c + word[s+1:]

                            if new == word:
                                continue
                            elif new == endGene and new in geneset:
                                return count
                            elif new in geneset:
                                que.append(new)
                                geneset.remove(new)
                count += 1
            return -1
        
        return gene()
                            

           