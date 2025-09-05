class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
            
        rows = len(matrix)-1
        cols = len(matrix[0])-1
        Frow = 0

        for i in range(rows+1):
            
            if matrix[i][0] == target:
                print("true thr first eleemnt")
                return True
            elif matrix[i][0] > target:
                Frow = i-1
                break
            elif matrix[i][0] < target:
                Frow = i
        print("this is Frow",Frow)     

        for i in range(cols+1):
            if matrix[Frow][i] == target:
                print("true through lowest element")
                return True
            elif matrix[Frow][i] < target:
                print("entered 111")
                
            elif matrix[Frow][i] > target:#search the column upwards
                print("searching up of this:",matrix[Frow][i])
                itr = Frow
                while itr >= 0:
                    print("entered 222")
                    if matrix[itr][i] == target:
                        print("true thr upsearch")
                        print("its:",matrix[Frow][i])
                        return True
                    else :
                        itr -= 1
                
                
        print("return false thr not present")
        return False
