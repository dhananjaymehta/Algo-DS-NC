class Solution:
    def maxArea(self, nums: List[int]) -> int:
        # goal -> maximize water
        # water capacity => Area 
        # i -> left boundry | j -> right boundry
        # Area = min(i, j) * (j-i) -> Maximize
        n=len(nums)
        l, r = 0, n-1
        max_capacity=0
        while l<r:
            capacity = self._capacity(nums, l, r)
            max_capacity=max(max_capacity, capacity)
            # l_capacity = self._capacity(nums, l+1, r)
            # r_capacity = self._capacity(nums, l, r-1)
            # print(capacity, l_capacity, r_capacity, max_capacity)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1
        return max_capacity

    def _capacity(self, nums, i, j):
        return min(nums[i], nums[j]) * (j-i)

    