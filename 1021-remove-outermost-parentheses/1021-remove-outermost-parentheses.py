class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        '''
        # here we track the depth with stack
        # If depth > 1, we pop and resolve

        if depth > 1 : append every cancellation into the string. 
        if depth = 1 and char == ')' cancel withou appending 
        if not stack, push without appending
        '''


        def remove_outer():
            result = ''
            stack = []

            for char in s:
                if not stack:
                    stack.append(char)
                elif len(stack) == 1 and char == ')':
                    stack.pop()
                else:
                    if char == '(':
                        stack.append(char)
                        result += char
                    if char == ')':
                        stack.pop()
                        result += char
            return result
        return remove_outer()