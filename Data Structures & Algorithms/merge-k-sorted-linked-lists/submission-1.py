# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)<1:
            return None
        
        res = ListNode(0) # dummy head
        cur = res # pointer
        minHeap = [] # heap
        
        for i, li in enumerate(lists):
            if li is not None:
                # Initial push: (value, tie-breaker-index, node)
                heapq.heappush(minHeap, (li.val, i, li))
                # Why tiebreaker? 
                # Python in case of tie fall to second item in tuple, 
                # So , TypeError: '<' not supported between instances of 'NodeWrapper' and 'NodeWrapper'.
            
        # now head of each list has been added
        while minHeap:
            # keep traversing each node while its in minHeap
            val, i, node = heapq.heappop(minHeap)
            cur.next = node
            cur=cur.next
            
            # if there's another item in list, push it in Heap
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
                
        return res.next
