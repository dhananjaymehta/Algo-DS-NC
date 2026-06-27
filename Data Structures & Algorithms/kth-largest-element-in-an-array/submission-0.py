class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # insert elements into heap
        max_heap = []
        import heapq
        
        for n in nums:
            heapq.heappush(max_heap, -n)
        
        # evacuate k elements
        i = 0
        res = 0
        while i <k:
            res = -heapq.heappop(max_heap)
            i+=1
        return res
