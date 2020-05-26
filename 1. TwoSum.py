# easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range (i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         else:
        #             continue
        # O(n) hash map
        nums_to_map = {}   
        for i in range(len(nums)):
            dif_target = target - nums[i]
            if dif_target in nums_to_map:
                return [i, nums_to_map[dif_target]]
            else:
                nums_to_map[nums[i]]=i
