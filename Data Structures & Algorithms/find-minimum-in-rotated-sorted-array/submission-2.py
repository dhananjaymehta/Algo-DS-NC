class Solution:
    def findMin(self, nums: List[int]) -> int:
        ln = len(nums)
        l, r = 0, ln-1
        cnt=0
        if len(nums)<2:
            return nums[0]
        while l<=r:
            # mid = int((l+r+1)/2)
            mid = (l+r)//2
            print(nums, nums[mid])
            print(l, mid, r)
            # if mid < mid-1 : 
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            # if mid < mid + 1 -> right side sorted, so we need to see left side
            if nums[mid]<=nums[r]:
                r=mid-1
            else:
                l=mid+1

        return -1
