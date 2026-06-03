# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # With BST the tree is sorted
        # We don't need to traverse whole tree
        # if p, q > root then check right side
        # if p, q < root then check left side
        # else return current node
        # return self.traverseIter(root, p, q)
        return self.traverseRecur(root, p, q)
    
    def traverseIter(self, root, p, q):
        cur = root
        while cur:
            if cur.val<p.val  and cur.val<q.val:
                cur=cur.right
            elif cur.val>p.val  and cur.val>q.val:
                cur=cur.left
            else:
                return cur
    def traverseRecur(self, root, p, q):
        if not root:
            return None
        if root.val<p.val and root.val<q.val:
            return self.traverseRecur(root.right, p, q)
        elif root.val>p.val and root.val>q.val:
            return self.traverseRecur(root.left, p, q)
        else:
            return root