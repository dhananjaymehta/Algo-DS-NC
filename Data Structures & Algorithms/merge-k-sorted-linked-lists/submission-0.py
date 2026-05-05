# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# class NodeWrapper:
#     def __init__(self, node):
#         self.node = node
    
    # def __lt__(self, other):
    #     return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)<1:
            return None
        
        res = ListNode(0) # dummy head
        cur = res # pointer
        minHeap = [] # heap
        
        for i, li in enumerate(lists):
            if li is not None:
                heapq.heappush(minHeap, (li.val, i, li))
            
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
