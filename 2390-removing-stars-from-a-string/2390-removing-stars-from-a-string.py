class Solution:
    def removeStars(self, s: str) -> str:
        
        def starless():
            stack = []

            for char in s:
                if char == '*':
                    stack.pop()
                else:
                    stack.append(char)

            return "".join(stack)
        
        return starless()
        