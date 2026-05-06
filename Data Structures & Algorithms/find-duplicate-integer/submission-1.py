class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # "Tortoise and Hare" (slow and fast pointers) method
        # Phase 1: Detect the Cycle
        # Phase 2: Find the duplicate
        """
        Phase 1: Detect the Cycle
        Start two pointers, slow and fast, at the first element (nums[0]).

        Move slow one step at a time: slow = nums[slow].

        Move fast two steps at a time: fast = nums[nums[fast]].

        They are guaranteed to meet at some point inside the cycle.
        """
        slow = fast = 0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                break
        
        """
        Phase 2: Find the Duplicate (Cycle Entrance)
        Once they meet, keep fast where it is, but reset slow to the very beginning (nums[0]).

        Move both slow and fast exactly one step at a time.

        The exact point where they meet again is the duplicate number.
        """
        slow=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            if fast==slow:
                break
        # print(slow, fast)
        # print(slow, fast)            
        return slow