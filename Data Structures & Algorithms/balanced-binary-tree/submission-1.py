# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        # get height left, get height right
        # check height_diff(left vs right) < 2
        self.res = True
        
        def traverse_dfs(root):
            if not root:
                return 0
            l=traverse_dfs(root.left)
            r=traverse_dfs(root.right)
            if abs(r-l)>1:
                self.res=False
            return 1+max(l, r)
        
        traverse_dfs(root)
        return self.res