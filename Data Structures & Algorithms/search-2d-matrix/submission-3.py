class Solution:
    def via_staircase(self, matrix, row, col, target):        
        """
        Intuition
        Since each row is sorted left-to-right and each column is sorted top-to-bottom, we can search smartly instead of checking every cell.

        Start at the top-right corner:

        If the current value is greater than the target → move left (values decrease).
        If it is smaller than the target → move down (values increase).
        This works like walking down a staircase—each step eliminates an entire row or column.
        We keep moving until we either find the target or move out of bounds.

        Algorithm
        Let r = 0 (first row) and c = n - 1 (last column).
        While r is within bounds and c is within bounds:
        If matrix[r][c] == target, return true.
        If the value is greater than the target, move left (c -= 1).
        If the value is smaller, move down (r += 1).
        If we exit the matrix, the target is not found → return false.
        """
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