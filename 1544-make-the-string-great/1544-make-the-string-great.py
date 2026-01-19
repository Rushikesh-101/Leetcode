class Solution:
    def makeGood(self, s: str) -> str:
        
        '''
        Intuition : 
        '''
        def good_string():
            stack = []
            for char in s :
                if stack and stack[-1].islower() and char.islower():
                    stack.append(char)
                elif stack and stack[-1].isupper() and char.isupper():
                    stack.append(char)
                elif stack and stack[-1].lower() == char.lower():
                        stack.pop()
                else:
                    stack.append(char)
            
            return "".join(stack)
           
        return good_string()


            
                

