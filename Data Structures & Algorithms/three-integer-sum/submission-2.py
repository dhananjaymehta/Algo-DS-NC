class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array to be able to identify the items in increasing order
        nums.sort() 
        result = []
        n = len(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            found_pairs = self.twosum(nums[i+1:], nums[i], val=0-nums[i])            
            for l, r in found_pairs:
                result.append([nums[i], l, r])
        
        return result


    def twosum(self, nums, n, val):
        l, r = 0, len(nums)-1       
        pairs = []
        while l < r:
            if  nums[l] + nums[r] == val:
                pairs.append((nums[l], nums[r]))
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif nums[l] + nums[r] < val:
                l+=1
            else:
                r-=1
        return pairs