# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:                
        self.res = root.val
        self.counter = 0
        
        # recursive DFS - inorder traversal
        def traverseDFS(root, k):            
            if not root:
                return None
            # traverse left
            traverseDFS(root.left, k)            
            
            # Node: compare value
            if self.counter == k:
                return
            self.counter+=1
            if self.counter == k:
                self.res = root.val
                return
            
            # traverse right
            traverseDFS(root.right, k)            
        
        traverseDFS(root, k)
        return self.res
        # return -1