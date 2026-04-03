class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix, suffix = [1]*n, [1]*n
        
        res=[]
        i = 1
        while i < n:
            # Prefix: Product of everything to the left
            prefix[i] = prefix[i-1] * nums[i-1]
            
            # Suffix: Product of everything to the right
            # We use 'j' to mirror 'i' from the end of the array
            j = n - 1 - i
            suffix[j] = suffix[j+1] * nums[j+1]            
            i+=1
        
        i=0
        while i < len(nums):
            res.append(suffix[i]*prefix[i])
            i+=1
        
        return res


        