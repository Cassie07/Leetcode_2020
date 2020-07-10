class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res
    
    def dfs(self, nums, target, index, tmp):
        if target == 0:
            self.res.append(tmp)
            return
        
        if target > 0:
            for i in range(index, len(nums)):
                self.dfs(nums, target - nums[i], i, tmp + [nums[i]])
        else:
            return
