class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        
        if len(nums) == 0:
            self.res.append([])
        
        for i in range(len(nums)):
            self.dfs(i, [], nums)
            
        return self.res
    
    def dfs(self, i, tmp, no_visited):
        if len(no_visited) == 0:
            if tmp not in self.res:
                self.res.append(tmp)
            return
        
        if i < len(no_visited):
            tmp.append(no_visited[i])
            for k in range(len(no_visited)):
                copy_tmp = copy.deepcopy(tmp)
                self.dfs(k, copy_tmp, no_visited[:i] + no_visited[i+1:])
