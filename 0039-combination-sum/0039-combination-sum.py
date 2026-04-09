class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        options = candidates

        def recur(cand, tgt, opt):
            nonlocal result
            if tgt >= target:
                if tgt == target:
                    result.append(cand)
                return

            else:
                for i in range(len(opt)):
                    tgt += opt[i]
                    cand.append(opt[i])
                    recur(cand[:], tgt, opt[i:])
                    cand.pop()
                    tgt -= opt[i]
        tgt = 0
        cand = []
        recur(cand, tgt, options)
        return result