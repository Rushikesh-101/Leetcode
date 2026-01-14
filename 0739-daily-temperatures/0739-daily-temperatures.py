class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Basic next greater element stuff
        # Just store difference of indexes as result while popping from mono 

        def temp():

            mono = []
            result = []
            for i in range(len(temperatures)):
                result.append(0)

            for i in range(len(temperatures)):
                if not mono:
                    mono.append(i)
                else:
                    while mono and temperatures[mono[-1]] < temperatures[i]:
                        pop = mono.pop()
                        result[pop] = i-pop
                    mono.append(i)
            
            return result
        
        return temp()
           