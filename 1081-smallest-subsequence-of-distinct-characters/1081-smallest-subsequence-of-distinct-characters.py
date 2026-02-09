class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        # string subsequence mean : relative order but gaps allowed
        def smallest():
            mapp = {}
            for char in s:
                if char in mapp:
                    mapp[char] += 1
                else :
                    mapp[char] = 1
            print(mapp)


            stack = []
            exists = set()
            for char in s :
                if char in exists:
                    mapp[char] -= 1
                    continue
                while stack and stack[-1] > char and mapp[stack[-1]] >= 1 :
                    exists.remove(stack.pop())
                stack.append(char)
                exists.add(char)
                mapp[char] -= 1

            return "".join(stack)
        
        return smallest()
                