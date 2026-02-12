class Solution:
    def maximum69Number (self, num: int) -> int:
        
        def sus_number_69(num):
            num = str(num)
            for i in range(len(num)):
                if num[i] == '6':
                    result = num[:i]+'9'+num[i+1:]
                    return int(result)
            
            return int(num)
        return sus_number_69(num)
