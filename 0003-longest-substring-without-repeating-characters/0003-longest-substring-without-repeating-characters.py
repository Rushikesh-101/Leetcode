class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        def longest_substring():
            mapp = {}
            l = 0
            r = 0
            max_len = 0
            for r in range(len(s)):
                if s[r] in mapp:
                    mapp[s[r]] += 1
                else:
                    mapp[s[r]] = 1
                
                while mapp[s[r]] > 1:
                    mapp[s[l]] -= 1
                    l += 1
                
                max_len = max(max_len,(r-l)+1)
            
            return max_len
        
        return longest_substring()
                
