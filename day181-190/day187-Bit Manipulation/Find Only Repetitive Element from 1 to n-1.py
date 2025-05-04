class Solution:
    def findDuplicate(self, arr):
        #code here
        n=len(arr)
        xor_all=0
        xor_uniques=0
        for i in range(n-1):
            xor_all^=arr[i]
            xor_uniques^=(i+1)
        xor_all^=arr[n-1]
        return xor_all^xor_uniques
    
    def findDuplicate2(self, arr):
        #code here
        n=len(arr)
        xor=0
        for i in range(n-1):
            xor^=(i+1)^arr[i]
        xor^=arr[n-1]
        return xor
    
sol=Solution()
#arr = [1, 3, 2, 3, 4]
arr=[1, 1]  
print(sol.findDuplicate2(arr))
