class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # Sorting to avoid duplicates
        candidates.sort()
        result = []
        # No duplicates at same recursive level

        def recur(cand,array,tgt):
            nonlocal result
            print(cand,array,tgt)
            if tgt >= target:
                if tgt == target:
                    result.append(array[:])
                return 

            else:
                for i in range(len(cand)):

                    if i == 0 or cand[i-1] != cand[i]:

                        array.append(cand[i])
                        tgt += cand[i]
                        recur(cand[i+1:],array[:],tgt)
                        array.pop()
                        tgt -= cand[i]
        array = []
        recur(candidates,array,0)
        return result
        