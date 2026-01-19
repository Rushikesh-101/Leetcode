class Solution:
    def makeGood(self, s: str) -> str:
        
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

        '''
        # Or use ascii value difference
        # Lower case and upper case ascii diff of same char is 32

        def is_good():

            stack = []

            for char in s:
                if not stack:
                    stack.append(char)
                elif abs(ord(stack[-1]) - ord(char)) == 32:
                    stack.pop() 
                else:
                    stack.append(char)

            return "".join(stack)

        return is_good()
            
                

