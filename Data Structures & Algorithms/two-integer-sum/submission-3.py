class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # x(known) + y(unknow) = z(target)
        # y = z-x 
        check = dict()
        
        for n in range(len(nums)):
            if nums[n] in check:
                return [check.get(nums[n]), n]
            else:
                check[target-nums[n]]=n

        