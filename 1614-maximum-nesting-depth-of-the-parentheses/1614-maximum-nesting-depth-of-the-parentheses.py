class Solution:
    def maxDepth(self, s: str) -> int:
        # no of cancelations you make is the no of depth
        # after opening bracket the depth resets
        def dep():
            max_depth = 0
            stack = []
            for char in s:
                
                if char == ')' :
                    max_depth = max(len(stack),max_depth)
                    stack.pop()
                elif char == '(':
                    stack.append(char)
            return max_depth
        return dep()
                




