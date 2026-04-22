"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Iterative Solution
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        node_map = {None: None}
        
        iter1 = head
        # First pass: create copy of nodes        
        while iter1:
            copy = Node(iter1.val) # get the value of node
            node_map[iter1] = copy
            iter1 = iter1.next
        
        # for each node create a copy
        iter2 = head
        while iter2:
            copy = node_map[iter2]
            copy.next = node_map[iter2.next] # assign next node 
            copy.random = node_map[iter2.random] # assign random node
            iter2=iter2.next
        
        return node_map[head]
