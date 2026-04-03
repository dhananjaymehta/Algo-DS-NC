class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MinStack:
    from collections import deque

    def __init__(self):
        self.head=Node(None)
        self.min_val_stack = deque()        

    def push(self, val: int) -> None:
        item=Node(val)
        item.next=self.head.next
        self.head.next = item
        min_val = min(self.min_val_stack[-1], val) if self.min_val_stack else val
        self.min_val_stack.append(min_val)         

    def pop(self) -> None:        
        val=self.head.next.val
        self.head.next=self.head.next.next
        self.min_val_stack.pop() 
        

    def top(self) -> int:
        return self.head.next.val
        

    def getMin(self) -> int:
        return self.min_val_stack[-1]
        
