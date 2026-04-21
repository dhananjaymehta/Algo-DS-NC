# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if cycle then pointer return to original position
        # 2 pointers needed: one slow, one fast
        # if the two pointers meet then cycle
        # if fast pointer reach end then no cycle
        if not head:
            return False
        
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            # print(slow, fast)

        return False