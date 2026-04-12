class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:                        
        # handle lower bound of h
        if h<=len(piles):
           return max(piles)
        
        return self.search(piles, h)
        return -1
    
    def compute(self, piles, h, candidate):
        """ compute total hours for any input candidate"""
        total_h = 0
        for x in piles:
            total_h += math.ceil(x/candidate)
        return total_h
    
    def search(self, piles, h):
        """
        # h=4=> target
        # piles=[1,4,3,2]
        # potential k=[1, 2, 3, 4] 
        # find mid -> compute_time() x
        # compare x with h
        """
        l, r = 1, max(piles)
        res = r #. initialize
        while l<=r:
            mid = (l+r)//2
            h_val = self.compute(piles, h, mid)
            
            if h_val<=h:
                res = mid
                r=mid-1
            else:
                l=mid+1                            
        return res
        



