class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        braces = {'}': '{', ')': '(', ']': '['}
        stack = deque()
        for ch in s:
            if not ch in braces:
                stack.append(ch)
            else:
                # print(stack[-1], braces..get)
                if stack and stack[-1]==braces.get(ch):
                    stack.pop()
                else:
                    return False
            print(ch, stack)
                
        if stack:
            return False

        return True


        