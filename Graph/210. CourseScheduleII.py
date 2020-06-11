class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        graph = {i:[] for i in range(numCourses)}
        
        for child,parent in prerequisites:
            indegree[child] += 1
            graph[parent].append(child)
        
        source = deque()
        for i,j in indegree.items():
            if j == 0:
                source.append(i)
        print(source)
        res = []
        visited = 0
        while source:
            parent = source.popleft()
            res.append(parent)
            visited += 1
            for childs in graph[parent]:
                indegree[childs] -= 1
                if indegree[childs] == 0:
                    source.append(childs)
        return res if visited == numCourses else []
