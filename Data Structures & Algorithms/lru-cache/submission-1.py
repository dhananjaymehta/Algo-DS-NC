class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    from collections import defaultdict    
    def __init__(self, capacity: int):
        self.size=capacity        
        self.node_map = {}        
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:            
        # option 1: value don't exist, return -1
        if key not in self.node_map:
            return -1            
        # option 2: values exist, return val and update position
        else:
            node=self.node_map[key]
            # move the node to head
            self._remove(node)
            # move Node to head (recently used)
            self._add(node)
            return node.val  
        
    def put(self, key: int, value: int) -> None:
        print("put", key, value)
        # option 1: Node Exist
        if key in self.node_map:
            # update the value of node
            node=self.node_map[key]
            node.val= value
            # update value and move node to head            
            self._remove(node)
            self._add(node)
        # option 2: Node Don't exist
        else:
            node=ListNode(key, value)            
            # check if cache has space
            if len(self.node_map)<self.size:
                # add the value to cache
                self._add(node)                
            else:
                print("put", self.tail.prev.val)
                # step 1: eject the value from cache from tail
                self._eject()
                # step 2: add new value in the head
                # self._add(ListNode(key, value))
                self._add(node)
            self.node_map[key] = node
    
    def _add(self, node):
        temp = self.head.next
        # update the node        
        node.next=temp
        node.prev=self.head
        self.head.next=node
        temp.prev=node
    
    def _remove(self, node):
        # unlink pointers to the node
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _eject(self):
        # remove Least recently used item
        if len(self.node_map) == 0:
            return
        eject_node = self.tail.prev
        self._remove(eject_node)
        # remove item from map
        self.node_map.pop(eject_node.key, None)
