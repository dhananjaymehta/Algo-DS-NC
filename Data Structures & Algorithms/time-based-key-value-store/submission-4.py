class TimeMap:

    from collections import defaultdict
    def __init__(self):
        self.t_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.t_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # look up item
        if not key in self.t_map:
            return ''        
        # if availbale search val for timestamp 
        val = self.search(timestamp, self.t_map[key])
        return val
    
    def search(self,target,vals):        
        # search target in the values 
        l, r = 0, len(vals)-1
        res=""
        while l<=r:            
            mid=(l+r+1)//2
            ts, v = vals[mid]
            if ts<=target:                
                res=v
                l=mid+1
            else:                
                r=mid-1
        return res