class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.n = len(nums)
        
        if not nums:
            self.res.append([])
            
        for i in range(len(nums)):
            self.dfs(i, [], nums)
            
        return self.res
    
    def dfs(self, x, tmp, no_visit):  
        if x < len(no_visit):
            tmp.append(no_visit[x])
            for k in range(len(no_visit)):
                copy_tmp = copy.deepcopy(tmp)
                self.dfs(k, copy_tmp, no_visit[:x]+no_visit[x+1:])
            if len(tmp) == self.n:
                self.res.append(tmp)
        return
