class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        def shoot_arrows():
            if len(points) == 1:
                return 1
            points.sort(key = lambda x : (x[0],x[1]))
            print(points)
            arrows = 1
            for i in range(1,len(points)):
                if points[i][0] <= points[i-1][1]:
                    points[i][1] = min(points[i-1][1],points[i][1])
                else:
                    arrows += 1
            
            return arrows
        return shoot_arrows()
        '''

        # Trying a more optimal approach
        def shoot_arrowsV2():
            if len(points) == 1:
                return 1
            points.sort(key = lambda x : (x[0],x[1]))
            left = points[0][0]
            right = points[0][1]
            arrows = 1
            for i in range(1,len(points)):
                if points[i][0] <= right:
                    left = points[i][0]
                    right = min(right,points[i][1])
                else:
                    left = points[i][0]
                    right = points[i][1]
                    arrows += 1
            
            return arrows
        return shoot_arrowsV2()

