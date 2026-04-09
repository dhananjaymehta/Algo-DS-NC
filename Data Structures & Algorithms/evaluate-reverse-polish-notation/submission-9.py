class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return self.recursion_dfs(tokens)

    def recursion_dfs(self, tokens):
        token = tokens.pop()
        if token not in '+-*/':
            return int(token)
        right = self.recursion_dfs(tokens)
        left = self.recursion_dfs(tokens)        
        
        # encountered an operator
        if token == '+':
            return left + right
        elif token == '-':
            return left - right
        elif token == '*':
            return left * right
        elif token == '/':
            return int(left / right)