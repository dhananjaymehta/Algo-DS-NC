from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 1. Use a hash map to store [fingerprint] -> [list of words]
        groups = defaultdict(list)
        
        for s in strs:
            # 2. Create a count of each letter (a-z)
            count = [0] * 26
            for char in s:
                # Use ord() to map 'a' to 0, 'b' to 1, etc.
                count[ord(char) - ord('a')] += 1
            # print(count)
            # print(tuple(count))
            # 3. Convert list to a tuple (immutable) so it can be a dictionary key
            groups[tuple(count)].append(s)
            
        return list(groups.values())