# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # result = max (result, max_left_height + max_right_height)
        # max height = max(left height, right height)
        self.res = 0
        
        def traverse_dfs(root):
            # if no further child node
            if not root:
                return 0

            left = traverse_dfs(root.left)
            right = traverse_dfs(root.right)

            self.res = max(self.res, left+right)
            return 1+max(left, right)
        
        # traverse the tree
        traverse_dfs(root)
        return self.res

        