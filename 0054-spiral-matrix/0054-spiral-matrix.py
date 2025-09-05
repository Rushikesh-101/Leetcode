class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        right = len(matrix[0])-1
        botm = len(matrix)-1
        left = 0 
        print("right",right,"botm:",botm)
        Farr = []

        while left <= right and top <= botm :

            for i in range(left,right+1):
                Farr.append(matrix[top][i])
            top += 1
            print("this is Farr after top:",Farr)

            for i in range(top,botm+1):
                Farr.append(matrix[i][right])
            right -= 1
            print("this is Farr after right:",Farr)

            if botm >= top:
                for i in range(right,left-1,-1):
                    Farr.append(matrix[botm][i])
                botm -=1
                print("this is Farr after botm:",Farr)
            
            if right >= left:
                for i in range(botm,top-1,-1):
                    Farr.append(matrix[i][left])
                left += 1
                print("this is Farr after left:",Farr)
        
        print("this is final Farr:",Farr)
        return Farr