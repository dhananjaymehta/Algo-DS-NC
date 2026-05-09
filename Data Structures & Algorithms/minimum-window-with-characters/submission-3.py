class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ""

        # this is the required substr
        targetMap, windowMap = Counter(t), {k:0 for k in t}        
        # count req. chars        
        have, need = 0, len(targetMap) 
        # track result
        min_len, min_ind = len(s), (-1, -1)
        
        l, r = 0, 0        
        
        # first find the substring that has all the character 
        # then traverse all the way to end to find smallest
        while r<len(s):            
            ch = s[r]
            
            # icrease windowMap if valid character for comparison            
            if ch in windowMap:
                windowMap[ch]+=1
                # If s[r] is in countT and its count in window matches countT, increment have.
                # If all chars for key found i.e a:2 & a:1 not all found 
                if ch in windowMap and  targetMap[ch] == windowMap[ch]:
                    have+=1
            
            # When have == need, the window is valid:                
            while have==need:
                str_len = (r-l+1)
                if str_len<=min_len:
                    min_ind=(l,r)
                    min_len = str_len
                    
                # shrink the window
                # Then shrink from the left:                                
                # Decrease the count of s[l] in window.
                # If s[l] is in countT and its count in window falls below countT, decrement have.
                if s[l] in windowMap:  
                    windowMap[s[l]]-=1                    
                    if windowMap[s[l]] < targetMap[s[l]]:                    
                        have-=1
                # Move l right.
                l+=1
            r+=1

        l , r = min_ind
        return s[l : r + 1] if min_len != float("infinity") else ""
