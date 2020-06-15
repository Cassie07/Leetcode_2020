class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = (0 + nums[len(nums)-1]) * (nums[len(nums)-1] + 1) //2
        print(total)
        
        for i in nums:
            total -= i
        
        if total == 0 and len(nums) < nums[len(nums)-1]+1:
            return 0
        if total == 0 and len(nums) == nums[len(nums)-1]+1:
            return len(nums)
        
        return total
# Bit Manipulation   
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
