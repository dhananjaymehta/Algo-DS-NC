class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)<2:
            return [0]
        # retain the position in the stack
        pos_stack =[0]
        t_len = len(temperatures)
        output=[0]*t_len
        
        for i in range(1, t_len):
            print(temperatures[i], i, pos_stack, output)
            while pos_stack and temperatures[i]>temperatures[pos_stack[-1]]:
                print('inner', temperatures[i], pos_stack[-1], output)
                output[pos_stack[-1]]=i-pos_stack[-1]
                pos_stack.pop()
            pos_stack.append(i)
    
        return output
 