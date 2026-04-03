class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures)<2:
            return [0]
        # retain the position in the stack
        pos_stack =[]        
        output=[0]*len(temperatures)
        
        for i, v in enumerate(temperatures):            
            while pos_stack and v > pos_stack[-1][0]:
                stackV, stackI = pos_stack.pop()
                output[stackI]=i-stackI                
            pos_stack.append((v, i))
    
        return output
 