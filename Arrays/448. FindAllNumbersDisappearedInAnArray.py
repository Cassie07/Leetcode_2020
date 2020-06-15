class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        for i in nums:
            index = abs(i)
            nums[index - 1] = - abs(nums[index - 1])
        res = []
        for index,num in enumerate (nums):
            if num > 0:
                res.append(index+1)
        return res
#         # hash map
#         # TIME: O(n)
#         # Space: O(n)
#         maps = {i+1:0 for i in range(len(nums))}
        
#         for i in nums:
#             maps[i] += 1
            
#         res = []
#         for i,j in maps.items():
#             if j == 0:
#                 res.append(i)
#         return res
