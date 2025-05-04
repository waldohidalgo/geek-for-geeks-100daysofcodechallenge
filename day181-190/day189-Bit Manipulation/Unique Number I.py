class Solution:
    def findUnique(self, arr):
        # code here
        xor=0
        for i in arr:
            xor^=i
        return xor
    
sol=Solution()
arr=[2, 30, 2, 15, 20, 30, 15]
print(sol.findUnique(arr))