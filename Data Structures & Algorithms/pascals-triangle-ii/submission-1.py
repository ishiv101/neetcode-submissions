class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        else:
            old_row = [1, 1]
            j = 2
            for k in range(2, rowIndex + 1):
                new_row = [1]      
                for i in range(0, j - 1):
                    new_row.append(sum(old_row[i:i+2]))
                new_row.append(1)
                old_row = new_row
                j += 1


        return new_row

                
                

        
                
                   
        