class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        def reverse(word,p1,p2):

            if p1 >= p2 :
                return word
            temp = word[p1]
            word[p1] = word[p2]
            word[p2] = temp

            p1 += 1
            p2 -= 1

            return reverse(word,p1,p2)


     
        p1 = 0
        p2 = len(s)-1

        return reverse(s,p1,p2)