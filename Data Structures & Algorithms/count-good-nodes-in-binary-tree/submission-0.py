# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # find all path from root to node
        # traverse paths identified 
        # search O(n) + determine O(n)
        # ALTERNATIVE
        # starting from root determine which node is greater than root or last seen node 
        # if root.left > root -> update the last seen
        # if root.right > root -> update last seen
        return self.getPath(root)        
    
    def getPath(self, root):
        self.res = []
        def traverseDFS(root, lastSeen):
            print(self.res)
            if not root:
                return None
            if root.val >= lastSeen:
                self.res.append(root.val)
                traverseDFS(root.left, root.val)
                traverseDFS(root.right, root.val)
            else:
                traverseDFS(root.left, lastSeen)
                traverseDFS(root.right, lastSeen)
            return

        traverseDFS(root, root.val)
        return len(self.res)