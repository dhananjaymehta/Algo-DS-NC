class Solution:
    def via_staircase(self, matrix, row, col, target):        
        if row>len(matrix)-1 or col <0:
            return False
            
        corner = matrix[row][col]
        print(row, col, corner)
        if corner==target:
            return True        
        if corner > target:
            col-=1
            return self.via_staircase(matrix, row, col, target)
        else:
            row+=1
            return self.via_staircase(matrix, row, col, target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        row, col = 0, len(matrix[0])-1
        return self.via_staircase(matrix, row, col, target)        