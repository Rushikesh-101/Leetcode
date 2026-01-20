class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        def min_remove():
            stack = []
            for char in range(0,len(s)):
                if stack and  s[stack[-1]] == '(' and s[char] == ')':
                    stack.pop()
                elif s[char] == '(' or s[char] == ')':
                    stack.append(char)
                
            result = []
            invalid = set(stack)
            for i in range(0,len(s)):
                if i not in invalid:
                    result.append(s[i])
            
            return ''.join(result)
        return min_remove()

