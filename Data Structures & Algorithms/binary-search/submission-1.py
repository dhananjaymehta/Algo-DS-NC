class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # iterative
        l, r = 0, len(nums)-1
        cnt=0
        while l<=r:
            mid = int((l+r)/2)
            print(nums, nums[mid], l, r, mid)
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1            
            cnt+=1
            if cnt>10:
                break
        return -1