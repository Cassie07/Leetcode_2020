class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.k = k
        nums = [i+1 for i in range(9)]
        self.dfs(nums, n, 0, [])
        
        return self.res
    
    def dfs(self, nums, target, index, tmp):
        if target == 0 and len(tmp) == self.k:
            self.res.append(tmp)
            return
        
        if target > 0 and len(tmp) < self.k:
            for i in range(index, len(nums)):
                self.dfs(nums, target - nums[i], i + 1, tmp + [nums[i]])
        else:
            return
