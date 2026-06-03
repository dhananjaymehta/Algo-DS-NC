# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # using a BFS to traverse the tree
        # determine no. of elements in level before seeing the items
        # till the counter hold, add the items to list
        from collections import deque
        # item in a level
        visit = deque()
        visit.append(root)
        # no. of items in the level
        lv = len(visit)
        output = []
        while visit:
            level = []
            while lv>0:
                item = visit.popleft()
                if item:
                    level.append(item.val)
                # add items related to item popped
                    visit.append(item.left)                 
                    visit.append(item.right) 
                # reduce item seen
                lv-=1
            if len(level)>0:
                output.append(level)
            lv = len(visit)
        return output
