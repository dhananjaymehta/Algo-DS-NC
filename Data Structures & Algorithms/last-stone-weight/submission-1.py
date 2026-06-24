class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap 
        # remove top 2 items from the heap
        # pop items till there's 1 item left
        import heapq
        self.max_heap = []
        for i in stones:
            heapq.heappush(self.max_heap, -i)
        
        while len(self.max_heap)>1:
            x, y = -heapq.heappop(self.max_heap), -heapq.heappop(self.max_heap) 
            net_weight = x-y

            if net_weight>0:
                heapq.heappush(self.max_heap, -net_weight)
        
        return -self.max_heap[0] if len(self.max_heap)>0 else 0