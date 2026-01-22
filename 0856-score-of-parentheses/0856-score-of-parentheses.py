class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        def para_olympics():
            stack = []

            for char in s:

                if char == '(':
                    stack.append(char)
                
                else:
                    if stack[-1].isdigit():
                        num = int(stack.pop())*2
                        stack.pop() # removed the underlying bracket
                        while stack and stack[-1].isdigit():
                            num += int(stack.pop())
                        stack.append(str(num))
                    elif stack[-1] == '(':
                        stack.pop()
                        num = 1
                        while stack and stack[-1].isdigit():
                            num += int(stack.pop()) 
                        stack.append(str(num))
            print(stack)
            return int(stack.pop())
        
        return para_olympics()