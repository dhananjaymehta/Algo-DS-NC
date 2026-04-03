class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for a set of strings there has to be following conditions 
        # 1. same set of character
        # 2. same count of characters
        # cat & act -> a1c1t1
        # stop, pots -> o1p1s1t1
        # {o1p1s1t1: stop, pots, a1c1t1: cat, act}
        anagram_map = dict()
        for st in strs:
            key = self.generate_anagram_key(st)
            if key in anagram_map:
                anagram_map[key].append(st)
            else:
                anagram_map[key]=[st]

        return [v for k,v in anagram_map.items()]

    def generate_anagram_key(self, st):
        from collections import Counter        
        return ''.join(f'{c}{n}' for c, n in sorted(Counter(st).items()))        

