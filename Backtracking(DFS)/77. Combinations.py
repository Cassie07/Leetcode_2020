class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.k = k
        if n < 1:
            self.res.append([])
        
        for i in range(n):
            print([i+1 for i in range(i, n)])
            self.dfs(0, [], [i+1 for i in range(i, n)])
            
        return self.res
    
    def dfs(self, x, tmp, no_visit):
        if len(tmp) == self.k :
            cop = tmp[:]
            cop.sort()
            if cop not in self.res:
                self.res.append(tmp)
            return

        if x < len(no_visit):
            tmp.append(no_visit[x])
            for i in range(len(no_visit)):
                copy_tmp = copy.deepcopy(tmp)
                self.dfs(i, copy_tmp, no_visit[:x] + no_visit[x+1:])
        
