class Solution:
    def maxWater(self, arr):
        # code here
        l,r=0,len(arr)-1
        ct=0
        while l<=r:
            if arr[l]<=arr[r]:
                ct=max(ct,arr[l]*(r-l))
                l+=1
            else:
                ct=max(ct,arr[r]*(r-l))
                r-=1
        return ct
sol=Solution()
arr=[2]
print(sol.maxWater(arr))