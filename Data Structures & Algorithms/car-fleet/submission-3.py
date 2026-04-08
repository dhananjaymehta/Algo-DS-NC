class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)<2:
            return 1
        # import defaultdict        
        moves = [(p, s) for p, s in zip(position, speed)]
        moves.sort(key=lambda x:x[0])
        
        counter=1
        p, s = moves.pop()
        time = (target-p)/s
                
        while moves:
            prev_p, prev_s = moves[-1]
            prev_time = (target-prev_p)/prev_s            
            if prev_time>time:
                counter+=1
                time=prev_time
            moves.pop()
            
        return counter 
      