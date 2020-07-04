class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(': ')', '{' : '}', '[': ']'}
        for i in s:
            if i in dic.keys():
                stack.append(i)
            elif i in dic.values():
                if stack == [] or dic[stack.pop()] != i:
                    return False
            else:
                return False
        return True if len(stack) == 0 else False
