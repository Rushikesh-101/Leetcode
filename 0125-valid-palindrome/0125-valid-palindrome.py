class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s[0]:
            return False
        def checkPalindrome():
            print(len(s))
            front = 0
            back = len(s)-1
            result = True
            while front <= back :
                print(front)
                
                while front < len(s)-1 and s[front].isalnum() == False :
                    front += 1
                while back > 0 and s[back].isalnum() == False :
                    back -= 1
                if front > back:
                    break
                    
                if s[front].lower() == s[back].lower():
                    front += 1
                    back -= 1
                else:
                    result = False
                    break
            return result
        
        return checkPalindrome()
                
