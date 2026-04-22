# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head        
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        cnt = 1
        while fast:   
            print(cnt, fast.val, slow.val)         
            fast=fast.next
            if cnt>n:
                slow=slow.next
            else:
                cnt+=1
            
        slow.next = slow.next.next
        return dummy.next            

        