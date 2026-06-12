# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # max path sum is max of one of the following 
        # root 
        # root + left
        # root + right
        # root + left + right
        # flow - 
        # do a pre-order traversal
        # at each root node find max based on above options
        self.maxVal = float("-inf")
        
        def preOrder(root):
            if not root:
                return 0
            ro = root.val
            l = preOrder(root.left)
            r = preOrder(root.right)
            localMax = max(ro, ro+l, ro+r)
            self.maxVal = max(localMax, self.maxVal, ro+l+r)
            print(ro, l, r, localMax, self.maxVal)
            return localMax
        
        preOrder(root)
        return self.maxVal