class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for each point compute sqrt
        # set up a min heap
        # put sqrt, point into heap
        # pop K shortest items
        import heapq
        min_heap = []                
        # get distance - O(n)
        for point in points:
            dist = self.compute_distance(point)
            print(dist, point)
            heapq.heappush(min_heap, (dist, point))
        
        i, result = 0, []
        
        # get smallest:
        while i < k:
            dist, point = heapq.heappop(min_heap)
            result.append(point)
            i+=1
        return result
    
    def compute_distance(self, point: List[int])->int:
        import math    
        x, y = abs(point[0]), abs(point[1])        
        return round(math.sqrt(x**2+y**2), 6)