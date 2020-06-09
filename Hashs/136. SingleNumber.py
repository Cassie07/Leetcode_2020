class Solution:
    
# hash-table
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        
        for i,j in dic.items():
            if j == 1:
                return i
            else:
                continue

# Bit Manipulation
# Concept
# If we take XOR of zero and some bit, it will return that bit
# a⊕0=a
# If we take XOR of two same bits, it will return 0
# a⊕a=0
# a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
