class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        self.left = -1
        self.right = -1
        def left_binary_search(low, high, nums, target):
            
            if low <= high:
                mid = low + (high - low)//2

                if nums[mid] == target:
                    self.left = mid
                    return left_binary_search(low, mid - 1, nums, target)
                
                if nums[mid] < target:
                    return left_binary_search(mid + 1, high, nums, target)
                else:
                    return left_binary_search(low, mid - 1, nums, target)
            else:
                return -1
            
        def right_binary_search(low, high, nums, target):
            
            if low <= high:
                mid = low + (high - low)//2

                if nums[mid] == target:
                    self.right = mid
                    return right_binary_search(mid + 1, high, nums, target)
                
                if nums[mid] < target:
                    return right_binary_search(mid + 1, high, nums, target)
                else:
                    return right_binary_search(low, mid - 1, nums, target)
            else:
                return -1
            
        left_binary_search(0, len(nums) - 1, nums, target)
        right_binary_search(0, len(nums) - 1, nums, target)
        return [self.left, self.right]
