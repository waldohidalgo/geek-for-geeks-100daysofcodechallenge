from collections import defaultdict
class Solution:
    def exactlyK(self, arr, k):
        # complejidad n cuadrado
        n=len(arr)
        l=0
        ct=0
        hs=defaultdict(int)
        for r in range(n):
            hs[arr[r]]+=1
            while len(hs)>k:
                hs[arr[l]]-=1
                if hs[arr[l]]==0:
                    del hs[arr[l]]
                l+=1              
            if len(hs)==k:
                st=defaultdict(int)
                j=r
                while len(st)!=k:
                    st[arr[j]]+=1
                    if len(st)==k:
                        ct+=(j-l+1)
                        break
                    j-=1
        return ct 

    def  exactlyK2(self, arr, k):
        # complejidad n
        def atMostK(arr,k):
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
        return atMostK(arr,k)-atMostK(arr,k-1)  
    
sol=Solution()
arr=[1, 2, 2, 3]
k=3
# arr= [1, 2, 2, 3]
# k = 2
# arr = [3, 1, 2, 2, 3]
# k = 3
print(sol.exactlyK(arr,k))
print(sol.exactlyK2(arr,k))