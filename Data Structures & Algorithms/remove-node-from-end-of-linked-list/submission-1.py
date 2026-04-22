# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow=dummy
        fast=head
        cnt = 1
        while fast:               
            fast=fast.next
            if cnt>n:
                slow=slow.next
            else:
                cnt+=1
            
        slow.next = slow.next.next
        return dummy.next            

        