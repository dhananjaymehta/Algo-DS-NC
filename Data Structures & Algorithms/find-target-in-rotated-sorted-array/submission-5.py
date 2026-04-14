class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # rotated array = 2 sorted_array (arr1+Pivot+arr2)    
        
        pivot = self.find_pivot(nums, target)
        print(pivot)
        idx = self.find_item(nums, pivot, target)
        return idx

    # find pivot
    def find_pivot(self, nums, target):
        # l, r = 0, len(nums)-1
        # while l<r:
        #     mid=(l+r+1)//2
        #     if nums[mid]< nums[r]:
        #         r=m
        #     else:
        #         l=mid+1
        # return l

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return l
    
    # find item
    def find_item(self, items, pivot, target):
        l, r = 0, len(items) - 1

        if target >= items[pivot] and target <= items[r]:
            l = pivot
        else:
            r = pivot - 1

        print(items)
        while l<=r:
            mid = (l+r)//2
            if items[mid]==target:
                return mid
            if items[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1        