class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        sqr = n*n
        rows = n
        cols = n
        top,left = 0 , 0
        botm,right = n-1, n-1
        intgr = 1

        
        matrix = [[0 for _ in range(n)] for _ in range (n)]
        


        while top <= botm and left <= right:

            for i in range(left,right+1):
                matrix[top][i] = intgr
                print("changing top",matrix,"with:",intgr)
                intgr += 1
            top += 1

            for i in range(top,botm+1):
                matrix[i][right] = intgr
                print("changing right",matrix,"with:",intgr)
                intgr += 1
            right -= 1
            
            if top <= botm:
                for i in range(right,left-1,-1):
                    matrix[botm][i] = intgr
                    print("changing botm",matrix,"with:",intgr)
                    intgr += 1
                botm -= 1

            if left <= right:
                for i in range(botm,top-1,-1):
                    matrix[i][left] = intgr
                    print("changing left",matrix,"with:",intgr)
                    intgr += 1
                left += 1 
            
        return matrix
