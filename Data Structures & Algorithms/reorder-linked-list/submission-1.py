# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]
        # L = [0, 1, 2, 3] R=[n-1, n-2, n-3]
        # new - L0 -> R0 -> L1 -> R1
        # [0, 1, 2, 3, 4, 5, 6]
        # [0 -> 1 ->2 ->3 <- 4 <-5 <-6]
        # 0 : new.next ->0; new.next.next = 6
        # 1 : new.next ->1; new.next.next = 5
        # 2 : new.next ->3; new.next.next = 4
        # Approach
        # reverse the node mid way
        # two headers start , end
        # move two headers simultaenously till midpoint
        mid = head
        start = head
        fast = head # stops at midpoint
        n = 1 # len of linkedlist
        # part 0: find midpoint
        while fast and fast.next:            
            mid=mid.next
            fast=fast.next.next
            n+=1

        # print(n, mid.val) 
        
        # part 1: reverse midpoint
        # mid is mid point
        end = None
        while mid:
            # print(mid.val)
            nxt = mid.next
            mid.next = end
            end=mid
            mid=nxt
        # print(end.val)
        
        # part 2: traverse the list
        cnt=0
        dummy=ListNode()
        new=dummy
        # while cnt<n:            
        while start and end:            
            # new.next=start
            # new.next.next=end
            # print(start.val, end.val)
            if cnt%2==0:
                new.next=start
                start=start.next
            else:
                new.next=end
                end=end.next            
            cnt+=1
            # print(new.val)
            new=new.next
            # print(new.next.val, new.next.next.val)
            # new=new.next.next            
            # cnt+=1
            
            
        # return dummy.next
