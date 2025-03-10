class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        if m*k>len(arr):
            return -1
        mx=max(arr)
        for d in range(1,mx+1):
            buckets_count=0
            flowers_count=0
            for flower in arr:
                if flower<=d:
                    flowers_count+=1
                    if flowers_count==k:
                        flowers_count=0
                        buckets_count+=1
                        if buckets_count==m:
                            return d
                else:
                    flowers_count=0
        return -1
    
    def minDaysBloom2(self, m, k, arr):
        if m*k>len(arr):
            return -1
        l,r=1,max(arr)
        while l<=r:
            mid=(l+r)//2
            count=0
            flowers_count=0
            for flower in arr:
                if flower<=mid:
                    flowers_count+=1
                    if flowers_count==k:
                        flowers_count=0
                        count+=1
                        if count>=m:
                            break
                else:
                    flowers_count=0
            if count>=m:
                r=mid-1
            else:
                l=mid+1
        return l
    
# arr=[1, 10, 3, 10, 2]
# m=3
# k=2
arr,m,k=[3, 4, 2, 7, 13, 8, 5],3,2
#arr,m,k=[5, 5, 5, 5, 10, 5, 5],2,3
sol=Solution()
print(sol.minDaysBloom(m,k,arr))
print(sol.minDaysBloom2(m,k,arr))