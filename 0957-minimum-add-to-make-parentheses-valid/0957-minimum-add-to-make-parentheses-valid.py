class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        paraStack = []
        for n in s :

            if not paraStack :
                paraStack.append(n)

            elif n == ')' :

                if paraStack and paraStack[-1] == '(' :
                    paraStack.pop()
                
                else :
                    paraStack.append(n)
            
            else :
                paraStack.append(n)

        return len(paraStack)

