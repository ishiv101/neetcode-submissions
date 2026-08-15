class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # must return nothing, modify exisiting matrix
        rows = len(matrix)
        columns = len(matrix[0])

        # pass through matrix the first time to find which columns and rows to set to zero. Dont want to wipe out the whole matrix
        row_changes = set()
        column_changes = set()

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    row_changes.add(r)
                    column_changes.add(c)

        # pass through matrix second time to update it
        for num in row_changes:
            matrix[num] = [0] * columns
                
        for num in column_changes:
            for i in range(rows):
                matrix[i][num] = 0 


        

         
        
        