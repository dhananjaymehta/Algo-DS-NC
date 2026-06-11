# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # at each level check 
        # left: is node lower than root
        # right: is node greater than root
        self.is_valid = True

        def traverseDFS(root, valMin, valMax):
            if not root:
                return True           
            if not (valMin < root.val < valMax):
                return False
            return traverseDFS(root.left, valMin, root.val) and traverseDFS(root.right, root.val, valMax)
        
        return traverseDFS(root, float("-inf"), float("inf"))
        # return self.is_valid


                
        