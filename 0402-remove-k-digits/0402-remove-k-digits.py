class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Greedy approach : stack up digits, pop stack if current smaller than [-1]
        def remove_k(k):
            stack = []
            for s in num:
                
                while stack and int(stack[-1]) > int(s) and k:
                    stack.pop()
                    k -= 1
                if not stack and s == '0':
                    continue
                stack.append(s)
            while k and stack:
                stack.pop()
                k -= 1

            if stack:
                return "".join(stack) 
            else:
                return  '0'
        
        return remove_k(k)
            