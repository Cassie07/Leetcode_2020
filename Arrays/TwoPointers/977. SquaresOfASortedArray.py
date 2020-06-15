class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # # time: O(nlogn)
        # # space: N
        # A = [abs(i) * abs(i) for i in A]
        # A.sort()
        # return A
    
        # two pointers
        res = []
        # negtive:
        neg_end = 0
        for index, num in enumerate(A):
            if num >= 0:
                break
            else:
                neg_end = index
                
        pos_start = neg_end + 1
        if pos_start == len(A):
            return [i*i for i in A]
        
        while neg_end >= 0 and pos_start < len(A):
            neg = A[neg_end] **2
            pos = A[pos_start] ** 2
            if pos < neg:
                res.append(pos)
                pos_start += 1
            elif pos > neg:
                res.append(neg)
                neg_end -= 1
            else:
                res.append(neg)
                res.append(pos)
                pos_start += 1
                neg_end -= 1
        
        while neg_end >= 0 :
            res.append(A[neg_end]**2)
            neg_end -= 1
            
        while pos_start < len(A) :
            res.append(A[pos_start]**2)
            pos_start += 1
            
        return res
