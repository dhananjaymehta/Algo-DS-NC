class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        # traverse through the string
        # set a start and end of the string
        # use a map to capture the unique characters
        # if a new character show up move the head -> eject till the character not there anymore

        char_set = set()
        N = len(st)
        s, f = 0, 0
        max_len = 0
        if len(st)<2:
            return len (st)
        # xyzyz
        # char_set -> x | x, y | x, y, z
        # when you see y-> eject x, eject y now also increase s
        while f<len(st):
            if st[f] not in char_set:
                char_set.add(st[f])
                f+=1
            else:
                max_len = max(max_len, f-s)
                while st[f] in char_set and s<len(st):
                    char_set.remove(st[s])
                    s+=1
        
        return max(max_len, f-s)
