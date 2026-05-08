class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        char_map = {}
        max_len = 0  
        
        while r<n: 
            # increase count of character
            char_map[s[r]]=1+char_map.get(s[r],0)            
            # if r pointer move -> increase the count of char in map
            # if length - max_occurance <=k r increase
            # if l pointer moves -> decrease the count of char in map
            while ((r-l+1) - max(char_map.values()) > k):
                char_map[s[l]]-=1
                l+=1
            max_len = max (max_len, r-l+1)
            r+=1
        
        return max (max_len, r-l)