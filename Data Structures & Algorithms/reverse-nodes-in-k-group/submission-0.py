# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # boundry for rotation is prev and kth.next
        groupPrev = dummy
        
        # keep running till the end
        while True:
            kth = self.getkth(groupPrev, k)
            if not kth:
                break
            # set boundry upper limit
            groupNext = kth.next
            # Set prev to groupNext to not disconnect the group
            # [3->2->1]->[4->5->6]->[7]
            prev = groupNext
            curr = groupPrev.next
            
            # unless curr reach the boundry, revert
            while curr!=groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # update the groupPrev, this is to start of next group
            """
            Line 1: tmp = groupPrev.next
            Action: tmp now points to Node 1.

            Reason: Node 1 is currently the "tail" of the group we just fixed. It will be the "anchor" (the groupPrev) for the next group (4, 5, 6). We save it now because we are about to lose the reference to it.

            Line 2: groupPrev.next = kth
            Action: Dummy now points to Node 3.

            Result: This is the magic "stitch." The list now looks like: Dummy -> 3 -> 2 -> 1 -> 4...

            Why: We have successfully connected the previous part of the list to the new, reversed head.

            Line 3: groupPrev = tmp
            Action: groupPrev moves from Dummy to Node 1.

            Reason: In the next loop iteration, when we call getkth(groupPrev, 3), we want to start counting from Node 1 so we can find Node 4, 5, and 6.
            """
            tmp = groupPrev.next # hold pointer to first item 1
            groupPrev.next = kth # update dummy to point to next
            groupPrev = tmp      # updte dummy
        
        return dummy.next
    
    def getkth(self, curr, k):
        # get the kth element -> boundry
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr