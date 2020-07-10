class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.dfs(candidates, target, 0, [])
        return self.res
        
    def dfs(self, candidates, target, index, tmp):
        if target == 0:
            tmp.sort()
            if tmp not in self.res:
                self.res.append(tmp)
            return
        if target > 0:
            for i in range(index, len(candidates)):
                self.dfs(candidates[:i] + candidates[i+1:], target - candidates[i], i, tmp + [candidates[i]])
        else:
            return
