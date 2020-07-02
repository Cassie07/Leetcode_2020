class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums: return nums.index(target)
        c = 0
        for i in nums:
            if i < target:
                c += 1
        return c
