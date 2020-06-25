class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[0:k]
        elif x >= arr[len(arr) - 1]:
            return arr[len(arr) - k: len(arr)]
        else:
            close_index = self.find_index(0, len(arr) - 1, arr, x)
            print(close_index)
            l,r = close_index, close_index
            while r - l < k:
                if l == 0: return arr[l: l + k]
                if r == len(arr): return arr[r - k: r]
                if x - arr[l - 1] > arr[r] - x:
                    r += 1
                else:
                    l -= 1
            return arr[l:r]

            
    def find_index(self, l, r, arr, x):  
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l
                
