class Solution:
    def removeDuplicates(self, s: str) -> str:
        List1 = []
       
        for chr in s :
           
            if List1 and List1[-1] == chr:
                List1.pop()

            else :
                List1.append(chr)
        List2 = ''.join(List1)
        return List2