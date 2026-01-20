class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        negative checking stack for positive will explode
        positive checking stack for negative will not
        cause of the give directions 
        '''


        def aster():
            stack = []
            for aster in asteroids:

                if stack and stack[-1] > 0 and aster < 0:

                    while stack and stack[-1] > 0 and aster < 0:
                        if stack[-1] < abs(aster):
                            stack.pop()
                            continue
                        elif stack[-1] == abs(aster):      
                            stack.pop()
                            break
                        else:
                            break
                    else:
                        stack.append(aster)
                    

                else:
                    stack.append(aster)
                
            return stack
        return aster()
