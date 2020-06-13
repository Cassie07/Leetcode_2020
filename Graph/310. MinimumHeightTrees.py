class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        adj = {i:[] for i in range(n)}
        
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        leaves = [i for i in adj.keys() if len(adj[i]) == 1]
        
        
        while n > 2 :
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i][0]
                adj.pop(i)
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
    
  
