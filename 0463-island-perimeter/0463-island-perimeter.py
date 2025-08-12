class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        print("this is row lenght:",row)
        col = len(grid[0])
        print("this is column lenght:",col)
        Perimeter = 0
        for r in range(row):
            for c in range(col):
                
                if grid[r][c] == 1 : # Its a land

                    Perimeter += 4

                    if r != (len(grid)-1) and grid[r+1][c] == 1:
                        Perimeter -= 1
                    if r != 0 and grid[r-1][c] == 1:
                        Perimeter -= 1
                    if c != (len(grid[0])-1) and grid[r][c+1] == 1:
                        Perimeter -= 1
                    if c != 0 and grid[r][c-1] == 1:
                        Perimeter -= 1
                    print("\n",Perimeter," this is perimeter after :",r,c,)

                else :
                    print("\nthis block doesnt count")

        print("\nThis is the final perimeter: ", Perimeter)
        return Perimeter