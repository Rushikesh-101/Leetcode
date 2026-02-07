class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
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

