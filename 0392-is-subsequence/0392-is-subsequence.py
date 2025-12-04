class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        def subsequence(s,t,sPtr,tPtr):
            if sPtr >= len(s):
                return True

            if tPtr >= len(t):
                return False

            if s[sPtr] == t[tPtr]:
                sPtr += 1
                tPtr += 1 
                return subsequence(s,t,sPtr,tPtr)
                
            else:
                tPtr += 1
                return subsequence(s,t,sPtr,tPtr)
            
        return subsequence(s,t,0,0)
            