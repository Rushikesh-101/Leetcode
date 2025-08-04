class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = 0
        counter = 0
        for n in nums :

            if majority == 0 :
                majority = n
                counter+=1
                print("\n counter right now :", counter)
                print("\n majority right now :", majority)

            elif n != majority :
                if counter == 0:
                    majority = n
                    counter = 1
                else :
                    counter -= 1
            
            elif n == majority :
                counter+=1
            
        return majority
    
            