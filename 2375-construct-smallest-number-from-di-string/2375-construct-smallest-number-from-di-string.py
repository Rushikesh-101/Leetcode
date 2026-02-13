class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        # insert into stack one by one in increasing order, whenever I encountered, pop by resvering stack
        

        def DID():
            res = ''
            num = 0
            stack = []
            
            for i in range(len(pattern)):
                num += 1
                if pattern[i] == 'I':
                    res += str(num)
                    while stack:
                        res += str(stack.pop())
                    
                elif pattern[i] == 'D':
                    stack.append(str(num))
            
            num += 1
            res += str(num)
            while stack:
                res += str(stack.pop())
            
            
            return res
        
        return DID()

            
