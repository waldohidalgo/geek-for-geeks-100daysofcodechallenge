from collections import defaultdict

class Solution:
    def atMostK(self, arr, k):
        # Code here
        n=len(arr)
        ct=0
        w=1
        while w<=n:
            hs=defaultdict(int)
            for i in range(w):
                hs[arr[i]]+=1
            ct+=(len(hs)<=k)
            for j in range(w,n):
                hs[arr[j]]+=1
                hs[arr[j-w]]-=1
                if hs[arr[j-w]]==0:
                    del hs[arr[j-w]]
                if len(hs)<=k:
                    ct+=1
            w+=1
        return ct
    
    def atMostK2(self,arr,k):
        n=len(arr)
        ct=0
        l=0
        hs=defaultdict(int)
        for r in range(n):
            hs[arr[r]]+=1
            while len(hs)>k:
                hs[arr[l]]-=1
                if hs[arr[l]]==0:
                    del hs[arr[l]]
                l+=1
            ct+=(r-l+1)
        return ct

            
            
    
sol=Solution()
arr=[1, 2, 1, 1, 3, 3, 4, 2, 1]
k=2
print(sol.atMostK(arr,k))
print(sol.atMostK2(arr,k))
