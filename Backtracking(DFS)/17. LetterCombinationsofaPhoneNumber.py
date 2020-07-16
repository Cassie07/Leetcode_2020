class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []
        self.dict = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8: ['t','u','v'], 9:['w','x','y','z']}
        self.length = len(digits)
        if '1' in digits or self.length == 0:
            return self.res
        self.digits = digits
        
        self.dfs(0, "")
        
        return self.res
    
    def dfs(self, key_index, tmp) :
        if len(tmp) == self.length:
            self.res.append(tmp)
            return 
        
        if key_index < self.length:
            candidate = self.dict[int(self.digits[key_index])]
            for i in range(len(candidate)):
                self.dfs(key_index + 1, tmp + candidate[i])
        else:
            return
