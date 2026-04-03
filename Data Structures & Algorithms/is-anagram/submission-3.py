class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        # if length vary return fals
        if len(s)!=len(t):
            return False
        # get count of character - O(n)
        s_map = self.get_char_map(s)
        t_map = self.get_char_map(t)
        # Pass if:
        # 1. char in on string exist in other 
        # AND 2. char count in one string ==char count in second

        for k,v in s_map.items():
            if k in t_map:
                if v == t_map.get(k):
                    continue
                else:
                    return False
            else:
                return False
        return True
        
    def get_char_map(self, st):
        return Counter(st)