class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        key_s1 = self.get_key(s1)        
        ls1 = len(s1)
        ls2 = len(s2)
        l, r = 0, ls1
        if len(s2)<len(s1):
            return False        
        while r<ls2:
            key = self.get_key(s2[l:r])
            print(key, key_s1)
            if key == key_s1:
                return True
            l+=1
            r+=1
        if self.get_key(s2[l:r]) == key_s1:
                return True
        return False

    def get_key(self, substr):
        items = sorted(Counter(substr).items())
    
        # Format as {v}{k} to get "1a2b1c"
        key = "".join(f"{v}{k}" for k, v in items)
        return key        