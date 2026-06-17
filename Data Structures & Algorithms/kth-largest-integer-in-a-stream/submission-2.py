
class KthLargest:    
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k = k        
        self.min_heap=[]
        
        for i in nums:
            self.add(i)

        

    def add(self, val: int) -> int:        
        # 1. Push the value. Let the heap sort it out.
        heapq.heappush(self.min_heap, val)            
        
        # 2. If the heap grew past size K, throw away the smallest element. 
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) 

        # 3. Index 0 is now guaranteed to be your K-th largest element.
        return self.min_heap[0]

    import heapq
