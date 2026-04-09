class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)<2:
            return int(tokens[-1])
        # A exp B -> [A, B, exp] // simplest unit
        # A is component that can unfol
        # tokens[-1]: exp | tokens[]
        ops = set(['+', '-', '*', '/'])
        computed=[]
        for item in tokens:
            if item not in ops:
                computed.append(item)
            else:
                r , l = computed.pop(),  computed.pop()
                val = self.compute(int(l), int(r), item)
                computed.append(val)
            print(computed)
        return computed[-1]

    def compute(self, l, r, operand):
        print(l, r, operand)
        if operand=='+':
            return l+r
        elif operand=='-':
            return l-r
        elif operand=='*':
            return l*r
        else:
            return int(l/r)