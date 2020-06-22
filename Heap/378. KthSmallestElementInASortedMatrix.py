class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                heap.append(matrix[i][j])
        heapq.heapify(heap)
        for i in range(k):
            res = heapq.heappop(heap)
        return res
