from collections import defaultdict

class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        res=[0]*(n-k+1)
        dis=defaultdict(int)
        s,e=0,k
        while s<e:
            dis[arr[s]]+=1
            s+=1
        res[0]=len(dis)
        for i in range(s,n):
            dis[arr[i]]+=1
            dis[arr[i-k]]-=1
            if dis[arr[i-k]]==0:
                del dis[arr[i-k]]
            res[i-k+1]=len(dis)
        return res
    
sol=Solution()
arr=[1, 1, 1, 1, 1]
k=5
print(sol.countDistinct(arr,k))
        
        