class Solution:
    def kokoEat(self,arr,k):
        # Code here
        mx=max(arr)
        for t in range(1,mx+1):
            count=0
            for elem in arr:
                count+=-(-elem//t)
                if count>k:
                    continue
            if count<=k:
                return t
    def kokoEat2(self,arr,k):
        # Code here
        l,r=1,max(arr)
        while l<r:
            mid=(l+r)//2
            count=0
            for elem in arr:
                count+=-(-elem//mid)
            if count<=k:
                r=mid
            else:
                l=mid+1
        return r
            
arr=[5, 10, 15, 20]
k=7
sol=Solution()
print(sol.kokoEat(arr,k))
print(sol.kokoEat2(arr,k))