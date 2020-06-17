class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        flag = True
        low = self.search(flag)
        flag = False
        high = self.search(flag) - 1
        print((low,high))
        if len(nums) == low or self.nums[low] != target:
            return [-1,-1]
        return [low, high]
    
    def search(self, flag):
        low = 0
        high = len(self.nums)
        
        while low < high:
            mid = low + (high-low)//2
            # when flag == True: find the first position of th number
            # mid > target: search in the left part
            # mid == target: search in the left part
            if self.nums[mid] > self.target or (flag and self.nums[mid] == self.target):
                high = mid
            else:
                low = mid + 1
        return low
                
            
            
        # O(nlgn)
#         if len(nums) == 0:
#             return [-1,-1]
#         self.low = len(nums)-1
#         self.high = 0
#         self.nums = nums
#         self.target = target
#         self.flag = 0
#         self.BinarySearch(0,len(nums)-1)
#         if self.flag == len(nums):
#             return [-1, -1]
#         return [self.low, self.high]
        
    
#     def BinarySearch(self, left, right):
#         if left == right:
#             if self.nums[left] == self.target:
#                 if left < self.low:
#                     self.low = left
#                 if left > self.high:
#                     self.high = left
#             else:
#                 self.flag += 1
#             return
            
#         mid = left + (right-left) // 2
        
#         self.BinarySearch(left, mid)
#         self.BinarySearch(mid + 1, right)
