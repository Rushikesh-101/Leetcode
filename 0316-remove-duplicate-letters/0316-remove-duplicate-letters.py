class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''

        - create freq map 
        - traverse and build a greedy stack by :
            - see if the character would appear again 

        '''

        def lexo():

            stack = []
            freq = {}
            visited = set()
            # Created the freq map
            for i in s:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
                
            # Now comparing char with stack[-1]
            for char in s:
                freq[char] -= 1
                if char in visited:
                    continue
                    
                else :
                    while stack and stack[-1] > char and freq[stack[-1]] > 0 :
                        visited.remove(stack.pop())
                    stack.append(char)
                    visited.add(char)
                
            return ''.join(stack)
                
        return lexo()