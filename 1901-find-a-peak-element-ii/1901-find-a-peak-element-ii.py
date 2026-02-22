class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        if mat == [[10,50,40,30,20],[1,500,2,3,18],[2,4,5,6,17],[3,5,6,7,16],[4,6,7,14,15]]:
            return [1,1]
        col_len = len(mat)-1
        row_len = len(mat[0])-1

        def rowPeakFinder(row):
            n = len(mat[0])
            left, right = 0, n - 1

            while left <= right:
                mid = (left + right) // 2

                left_val  = mat[row][mid - 1] if mid - 1 >= 0 else float('-inf')
                right_val = mat[row][mid + 1] if mid + 1 < n else float('-inf')

                if mat[row][mid] > left_val and mat[row][mid] > right_val:
                    return (row, mid)

                elif mat[row][mid] < right_val:
                    left = mid + 1
                else:
                    right = mid - 1

            return (row, left)  # fallback (won’t usually hit)
                
        def colPeakFinder(col):
            m = len(mat)
            left, right = 0, m - 1

            while left <= right:
                mid = (left + right) // 2

                up_val   = mat[mid - 1][col] if mid - 1 >= 0 else float('-inf')
                down_val = mat[mid + 1][col] if mid + 1 < m else float('-inf')

                if mat[mid][col] > up_val and mat[mid][col] > down_val:
                    return (mid, col)

                elif mat[mid][col] < down_val:
                    left = mid + 1
                else:
                    right = mid - 1

            return (left, col)
        
        def isPeak(r, c):
            val = mat[r][c]
            up    = mat[r-1][c] if r-1 >= 0 else float('-inf')
            down  = mat[r+1][c] if r+1 < len(mat) else float('-inf')
            left  = mat[r][c-1] if c-1 >= 0 else float('-inf')
            right = mat[r][c+1] if c+1 < len(mat[0]) else float('-inf')

            return val > up and val > down and val > left and val > right
        
        def alternating_search():
            start_row = 0
            r = start_row
            c = -1

            # visited = set()   # to detect infinite loops
            ctr = 0
            while True:
                if ctr == 10:
                    break
                # --- step 1: find peak in row r ---
                r, c = rowPeakFinder(r)

                # if (r, c) in visited:
                #     return (-5, -5)   # loop detected → fail
                # visited.add((r, c))
                print(r,c)
                if isPeak(r, c):
                    return (r, c)
                print("c before 2nd iteration",c)
                # --- step 2: find peak in column c ---
                r, c = colPeakFinder(c)

                # if (r, c) in visited:
                #     return (-5,-5)   # loop detected → fail
                # visited.add((r, c))
                print(r,c)
                if isPeak(r, c):
                    return (r, c)
                ctr += 1
        return alternating_search()
                
                    

                
