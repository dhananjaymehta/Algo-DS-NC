class Solution:
    def isPalindrome(self, st: str) -> bool:
        import string
        n = len(st)
        s, e = 0, n-1
        # Create the set
        char_set = set(string.ascii_letters + string.digits)
        # print(char_set)
        while s <= e:
            # check if left in ascii set
            if st[s] not in char_set:
                s+=1
                continue
            # check if right in ascii set
            if st[e] not in char_set:
                e-=1
                continue

            if st[s].lower()==st[e].lower():
                s+=1
                e-=1
            else:
                return False
        return True