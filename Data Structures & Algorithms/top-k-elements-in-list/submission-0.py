class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        cnt = Counter(nums)
        max_heap = []
        
        for key, val in cnt.items():
            heapq.heappush(max_heap, (-val, key))
        
        result = []
        while k>0:
            count, key = heapq.heappop(max_heap)
            result.append(key)
            k-=1
        return result
        


