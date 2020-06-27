class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                zero = i
                for j in range(i, len(nums)):
                    if nums[j]!= 0:
                        nums[zero], nums[j] = nums[j], nums[zero]
                        zero = j
        return nums
