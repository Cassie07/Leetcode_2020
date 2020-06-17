# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left < right:
            mid = left + (right - left) //2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
#         self.count = n
#         self.binary(1, n)
#         return self.count
    
#     def binary(self, low, high):
#         if low > high:
#             return
#         mid = low + (high - low) //2
#         if not isBadVersion(mid):
#             self.binary(mid+1, high)
#         else:
#             if mid < self.count:
#                 self.count = mid
#             self.binary(low, mid-1)
