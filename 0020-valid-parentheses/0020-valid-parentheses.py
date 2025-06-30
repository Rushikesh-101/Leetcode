class Solution:
    def isValid(self, s: str) -> bool:
        
        List = []

        # if len(s) == 1 or len(s) == 0 :
        #     return False 
        
        # else :
        for chr in s:

            if chr == '(':
                List.append(')')

            elif chr == '{':
                List.append('}')

            elif chr == '[':
                List.append(']')
            
            else :
                if len(List) == 0 or chr != List.pop():
                    return False

        if not List : 
            return True
        else :
            return False
