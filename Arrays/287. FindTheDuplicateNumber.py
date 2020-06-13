class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        # phase 1: interaction
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # phase 2: 
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        
        return slow
