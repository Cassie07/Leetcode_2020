class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        
        # BFS
        stack = deque()
        for i in range(len(graph)):
            if i not in colors.keys():
                colors[i] = 1
                stack.append(i)
                while stack:
                    node = stack.popleft()
                    for adj in graph[node]:
                        if adj not in colors.keys():
                            colors[adj] = -colors[node]
                            stack.append(adj)
                        else:
                            if colors[adj] == colors[node]:
                                return False
        return True
    
