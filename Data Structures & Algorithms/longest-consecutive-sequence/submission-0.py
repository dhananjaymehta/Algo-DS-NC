class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # next consecutive : n+1
        # next = {}
        # items -> if n-1 not in next{} -> its start and not next 
        
        # we only need to see if there is a n+1 for each n
        # n can either be start or next
        # n is start IF n-1 exist in numSet ELSE n is start

        # Create Set: to allow quick lookup O(1)
        numSet = set(nums)
        # keep track of longest
        max_long, longest = 0, 0                 
        
        for num in nums:
            # check if sequence
            if num-1 not in numSet:
                # start length 
                longest=1                
                while num+longest in numSet:

                    longest+=1
            max_long = max(max_long, longest)
        return max_long