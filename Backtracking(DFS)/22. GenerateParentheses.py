class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs("", n, n)
        return self.res
    
    def dfs(self, tmp, opens, close):
        if opens == 0 and close == 0: 
            self.res.append(tmp)
            return
        
        if opens < 0 or close < 0: return
        
        if opens > 0:
            self.dfs(tmp + "(", opens - 1, close)
            
        if close > opens:
            self.dfs(tmp + ")", opens, close - 1)
