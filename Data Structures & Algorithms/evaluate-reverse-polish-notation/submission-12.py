class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        

        def recursion_dfs():
            token = tokens.pop()
            if token not in '+-*/':
                return int(token)
            right = recursion_dfs()
            left = recursion_dfs()
            
            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return recursion_dfs()