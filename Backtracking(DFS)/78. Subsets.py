class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = [[]]
        self.nums = nums
        
        for i in range(len(nums)):
            self.dfs(i, [])
        return self.res
                
    def dfs(self, x, tmp):
        if x < len(self.nums):
            tmp.append(self.nums[x])
            self.res.append(tmp)
            new_tmp = copy.deepcopy(tmp) # if not use copy.deepcopy() tmp will be changed in the next iteration
            for k in range(x+1, len(self.nums)):
                new_tmp = copy.deepcopy(tmp)
                self.dfs(k, new_tmp)
                
