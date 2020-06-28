class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        n, m = len(board), len(board[0])
        for i in range(n):
            cur_index = 0
            for j in range(m):
                visited = []
                flag = self.dfs(i, j, cur_index, visited)
                if flag == True:
                    return True
                
        return False
        
    def dfs(self, n, m, cur_index, visited):
        if self.board[n][m] == self.word[cur_index]:
            visited.append((n,m))
            
            
            flag = flag2 = flag3 = flag4 = False
            
            if cur_index == len(self.word) - 1:
                return True
            
            tmp = visited
            if m + 1 < len(self.board[0]) and (n, m+1) not in visited:
                flag = self.dfs(n, m + 1, cur_index + 1, visited)
                if flag == False and (n, m + 1) in visited:
                    visited.remove((n, m + 1))
                    
            if m - 1 >= 0 and (n, m-1) not in visited:
                flag2 = self.dfs(n, m - 1, cur_index + 1, visited)
                if flag2 == False and (n, m - 1) in visited:
                    visited.remove((n, m - 1))
                    
            if n - 1 >= 0 and (n-1, m) not in visited:
                flag3 = self.dfs(n - 1 , m, cur_index + 1, visited)
                if flag3 == False and (n-1, m) in visited:
                    visited.remove((n-1, m))
                    
            if n + 1 < len(self.board) and (n+1, m) not in visited:
                flag4 = self.dfs(n + 1 , m, cur_index + 1, visited)
                if flag4 == False and (n+1, m) in visited:
                    visited.remove((n+1, m))

            return flag or flag2 or flag3 or flag4
        
        return False
