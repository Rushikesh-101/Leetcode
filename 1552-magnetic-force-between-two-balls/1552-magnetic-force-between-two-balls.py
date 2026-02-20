class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # minimum of maximum type question
        # will have upper bound
        position.sort()

        def gravity(mid):
            balls = m-1
            last = 0
            for i in range(1,len(position)):
                if position[i]-position[last] >= mid:
                    balls -= 1
                    last = i
                if balls == 0:
                    return True
            return False
        
        def magneto():
            left = 1
            right = position[-1] - position[0]

            while left < right:
                mid = (right+left+1)//2

                if gravity(mid):
                    left = mid
                else:
                    right = mid-1
            
            return left
    
        return magneto()
            