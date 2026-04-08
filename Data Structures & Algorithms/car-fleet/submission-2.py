class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)<2:
            return 1
        # import defaultdict        
        moves = []
        for i in range(len(position)):
            p, s = position[i], speed[i]    
            moves.append((p,s))

        moves.sort(key=lambda x:x[0])            
        print(moves)

        p, s = moves.pop()
        mv = (target-p)/s
        counter=1        
        while moves:
            pt, st = moves[-1]
            mvt = (target-pt)/st
            print("cur", p, s, mv, counter)
            print("peek", pt, st, mvt)
            if mvt>mv:
                counter+=1
                mv=mvt
            moves.pop()
            
        return counter 
      