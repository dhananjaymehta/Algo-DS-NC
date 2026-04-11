class Solution:
    def rec_binary_search(self, l, r, nums, target):        
        mid =  int((l+r+1)/2)
        # print(l,r, mid, nums, nums[mid])
        if l>r:
            return -1
        if nums[mid] == target:
            return mid
        # further action
        if nums[mid]<target:
            return self.rec_binary_search(mid+1, r, nums, target)
        return self.rec_binary_search(l, mid-1, nums, target)
                
    def search(self, nums: List[int], target: int) -> int:        
        return self.rec_binary_search(0, len(nums)-1, nums, target)