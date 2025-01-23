class Solution:
    def productExceptSelf(self, arr):
        #code here
        pf,sf=1,1
        n=len(arr)
        res=[1]*n

        for i in range(n):
            res[i]*=pf
            pf*=arr[i]

        for j in range(n-1,-1,-1):
            res[j]*=sf
            sf*=arr[j]
            
        return res
    


arr=[12, 0]
print(Solution().productExceptSelf(arr))