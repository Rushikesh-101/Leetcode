class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        oddVal = 0
        

        matrix = [ [ 0 for _ in range (n) ] for _ in range (m)]
        print(matrix)

        for i in indices :

            Urow = i[0]
            Ucol = i[1]

            for col in range (n):
                matrix[Urow][col] += 1

            for row in range(m):
                matrix[row][Ucol] +=1

            print("\n",matrix)
        

        for raw in range (m):
            for cal in range (n):
                if matrix[raw][cal] != 0 and (matrix[raw][cal])%2 != 0 :
                    oddVal += 1

        print("\n these many odd value : ",oddVal)
        return oddVal