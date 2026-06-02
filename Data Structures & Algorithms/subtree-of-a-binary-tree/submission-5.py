# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not subRoot:
#             return True
#         if not root:
#             return False
#         # going top down check
#         # if root itself is same means two tree are equal then return
#         if self.isSameTree(root, subRoot):
#             return True
        
#         # check if either left side or right side will have the subtree
#         return (self.isSameTree(root.left, subRoot) or 
#         self.isSameTree(root.right, subRoot))
    
    
#     def isSameTree(self,p, q):
#         if not p and not q:
#             return True        
#         # valid then traverse
#         if p and q and p.val == q.val:
#             return (self.isSameTree(p.left, q.left) and 
#             self.isSameTree(p.right, q.right))        
#         return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False