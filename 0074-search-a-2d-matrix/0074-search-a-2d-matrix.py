class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix :
            print("False thr empty")
            return False
    
        elif len(matrix) == 1: # single element or single list(1D array) 
            if len(matrix[0]) == 1 and matrix[0][0]==target:
                
                print("true thr singlet")
                return True
            elif len(matrix[0]) == 1 and matrix[0][0]!=target:
                print("false thr singlet")
                return False

            
            else :
                rows = len(matrix)-1
                cols = len(matrix[0])-1
                low = 0
                high = len(matrix[0])-1

                for i in range(cols+1):
                    mid = (low + high)//2
                    print("this is mid",mid)
                    if matrix[0][mid] == target:
                        print("true thr single array")
                        return True
                    elif matrix[0][mid] > target:
                        high = mid
                    elif matrix[0][mid] < target:
                        low = mid +1
                print("false thr single array")
                return False

                
        else :

            low = 0
            high = len(matrix)-1
            

            rows = len(matrix)-1
            cols = len(matrix[0])-1

            for i in range(rows+1):
                mid = (low + high)//2
                print("this is mid",mid)
                if matrix[mid][0] == target:
                    print("true")
                    return True
                elif matrix[mid][0] > target:
                    high = mid
                elif matrix[mid][0] < target:
                    print("value of mid :",mid,"value of cols:",cols)
                    if matrix[mid][cols] == target :
                        print("true thr last element")
                        return True
                    elif matrix[mid][cols] > target : # in same row
                        Nlow = 0
                        Nhigh = cols
                        for n in range(cols):
                            Nmid = (Nlow + Nhigh)//2
                            if matrix[mid][Nmid] == target :
                                print("true")
                                return True

                            elif matrix[mid][Nmid] > target:
                                Nhigh = Nmid
                            elif matrix[mid][Nmid] < target:
                                Nlow = Nmid+1


                    elif matrix[mid][cols] < target : # in next row
                        low = mid+1

            print("false")
            return False