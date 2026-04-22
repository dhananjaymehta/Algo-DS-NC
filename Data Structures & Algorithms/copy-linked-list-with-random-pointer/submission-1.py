"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Recursive Solution
    def __init__(self):
        self.seen_map = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        if head in self.seen_map:
            return self.seen_map.get(head)

        copy = Node(head.val)
        self.seen_map[head] = copy

        copy.next = self.copyRandomList(head.next)
        copy.random = self.seen_map.get(head.random)
        
        return copy
        