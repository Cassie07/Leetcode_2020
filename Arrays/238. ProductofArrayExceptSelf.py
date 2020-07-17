class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for i in range(len(nums))]
        
        # product items before nums[i]
        p = 1
        for i in range(len(nums)):
            out[i] *= p
            p *= nums[i]
            
        # product items after nums[i] 
        p = 1
        l = len(nums)
        while l > 0:
            out[l-1] *= p
            p *= nums[l-1]
            l -= 1
        return out
