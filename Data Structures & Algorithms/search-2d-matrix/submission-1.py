class Solution:
    def matrix_search_outer(self, matrix, l, r, target):        
        cnt=0
        while l<=r:
            mid=int((l+r+1)/2)
            lhs, rhs = matrix[mid][0], matrix[mid][-1]
            if lhs <= target and target<=rhs :
                return mid
            if target < lhs:
                r=mid-1
            else:
                l=mid+1
            cnt+=1
            if cnt>20:
                break
        return -1
    def matrix_search_inner(self, matrix, l, r, target):        
        cnt=0
        while l<=r:
            mid=int((l+r+1)/2)            
            if matrix[mid]==target:
                return mid
            if target < matrix[mid]:
                r=mid-1
            else:
                l=mid+1
            cnt+=1
            if cnt>20:
                break
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ind = self.matrix_search_outer(matrix, 0, len(matrix)-1, target)
        if ind > -1:            
            items = matrix[ind]
            ind_actual = self.matrix_search_inner(items, 0, len(items)-1, target)        
            return True if ind_actual > -1 else False
        else:
            return False
