class Solution:
    def maxWater(self, arr):
        # code here
        l,r=0,len(arr)-1
        ct=0
        mxl,mxr=0,0
        while l<=r:
            if mxl<=mxr:
                ct+=max(0,mxl-arr[l])
                mxl=max(mxl,arr[l])
                l+=1
            else:
                ct+=max(0,mxr-arr[r])
                mxr=max(mxr,arr[r])
                r-=1
        return ct
    
arr=[3, 0, 1, 0, 4, 0,2]
print(Solution().maxWater(arr))
