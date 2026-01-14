class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        def count_fruits():
            
            right = 1
            left = 0
            typea = fruits[left]

            while fruits[right] == typea and right < len(fruits)-1:
                right += 1
            typeb = fruits[right]
            max_len = right-left +1

            for right in range(1,len(fruits)):

                if fruits[right] == typea or fruits[right] == typeb:
                    max_len = max(max_len, (right-left)+1)
                else :
                    typeb = fruits[right]
                    left = right -1
                    typea = fruits[left]

                    while fruits[left-1] == typea or fruits[left-1] == typeb:
                        left -= 1

                    max_len = max(max_len, (right-left)+1)
            return max_len
        
        return count_fruits()
                        

                    
