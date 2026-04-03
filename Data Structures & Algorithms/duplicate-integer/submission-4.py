class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = dict()
        for i in nums:
            if i in seen: 
                return True 
            seen[i]=1
        return False
            
        