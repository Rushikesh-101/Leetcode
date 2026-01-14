class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a','e','i','o','u']

        total_count = 0
        curr_count = 0
        left = 0
        for i in range(k):
            if s[i] in vowels :
                curr_count += 1
        total_count = curr_count
    
        for right in range(k,len(s)):
            if s[left] in vowels :
                curr_count -= 1
            
            if s[right] in vowels :
                curr_count += 1

            left += 1

            total_count = max(total_count,curr_count)
        
        return total_count
    

    

             
