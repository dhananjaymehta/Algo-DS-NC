# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current point its next to previous
        # current move to forward
        # finally current reaches end => return current
        cur = head        
        prev= None
        cnt = 0
        
        while cur:
            forward=cur.next  # Forward stores next  node
            cur.next=prev     # Points to prev item
            prev=cur          # Assign cur node to prev
            cur=forward       # move cur to next locaton
        
        # prev returned as its to the end
        
        return prev
        