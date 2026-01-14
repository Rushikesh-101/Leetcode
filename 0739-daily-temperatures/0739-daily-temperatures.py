class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Basic next greater element stuff
        # Just store difference of indexes as result while popping from mono 

        def temp():

            mono = []
            result = [0]*len(temperatures)
            for i in range(len(temperatures)):
                
                while mono and temperatures[mono[-1]] < temperatures[i]:
                    pop = mono.pop()
                    result[pop] = i-pop
                mono.append(i)
            
            return result
        
        return temp()
           