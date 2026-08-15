class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #list result 
        result = []

        #extra 
        if not matrix:
            return result

        # boundaries
        top = 0
        right = len(matrix[0]) - 1
        left = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom: # makes sure no crossing over
            #traverse right 
            for i in range(left, right + 1):
                result.append(matrix[top][i]) #adds nums across top row
            top += 1 # shrinks top boundary

            #traverse down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right]) #along right column
            right -= 1 #shrinks right boundary 

            #traverse left

            if top <= bottom: #top shirnks earlier so need to check again 
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1 # shrinks bottom boundary

            # traverse up
            if left <= right: #right shrinks earlier so need to check again
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1 #shrink left boundary

        return result
        



         