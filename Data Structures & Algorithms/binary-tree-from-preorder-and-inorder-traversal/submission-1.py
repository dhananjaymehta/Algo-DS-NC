# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index_map = {val: index for index, val in enumerate(inorder)}
        
        def createTree(preorder, inorder):
            if not preorder or not inorder:
                return None
            
            node = preorder[0]
            root = TreeNode(node)
            # print(node, self.index_map, inorder)            
            mid = inorder.index(node)
            # get element left of root : preorder[1:mid+1] -> elements in Left after root
            root.left = createTree(preorder[1:mid+1], inorder[:mid])
            root.right = createTree(preorder[mid+1:], inorder[mid+1:])
            return root
        
        return createTree(preorder, inorder)