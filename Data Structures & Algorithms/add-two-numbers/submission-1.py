# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        dummy = ListNode(0)
        chk = dummy
        carry=0
        while a or b:
            # print(a.val, b.val, carry)
            if a and b:
                sum = a.val + b.val + carry
                carry, node_val = sum//10, sum%10
                print(sum, carry, node_val)
                node = ListNode(node_val)
                chk.next = node  
                a, b =a.next  , b.next             
            elif a:
                sum = a.val + carry
                carry, node_val = sum//10, sum%10
                node = ListNode(node_val)
                chk.next = node  
                a = a.next
            else:
                sum = b.val + carry
                carry, node_val = sum//10, sum%10
                node = ListNode(node_val)
                chk.next = node            
                b = b.next            
            
            # print(chk.val)
            chk=chk.next   
        # print(carry)
        
        if carry>0:
            node = ListNode(carry)
            chk.next = node  
            chk=chk.next   
        # print(chk.val)
        return dummy.next
