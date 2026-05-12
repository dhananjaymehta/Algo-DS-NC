class Solution:        
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # initalize the indexes for windows
        # set a max heap
        # insert the window into max heap as initialization 
        # move the window one element at a time l+1, r+1 -> 
        # before moving identify the  max element: if max element in valid range then pop else remove out of range max 
        # check the new element and insert it
        if len(nums)<1 or k<1:
            return []
        
        max_heap = []
        l, r = 0, 0
        res = []
        
        import heapq
        while r<len(nums):
            if (r-l+1)<k:
                heapq.heappush(max_heap, (-nums[r], r))
                r+=1
            else:
                # add next item in the heap
                heapq.heappush(max_heap, (-nums[r], r))
                # get max item of the heap
                val, max_heap = self.get_max_item(l, r, max_heap)
                res.append(val)
                l+=1
                r+=1                
            # print(l, r)
        return res

    def get_max_item(self, l, r, max_heap):
        # check if the top of heap is within the range
        # if not: while top not b/w l and r -> pop top
        # else: get the top item        
        val, ind = max_heap[0]
        
        while not (l <= ind <=r):            
            heapq.heappop(max_heap)
            val, ind = max_heap[0]                  
        
        val, ind = max_heap[0]
        
        return -val, max_heap
        