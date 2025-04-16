class Solution:   
    def peakElement(self,arr):
        n=len(arr)
        l,r=0,n-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]<arr[mid+1]:
                l=mid+1
            else:
                r=mid
        return l
    
sol=Solution()
arr=[1,2,4,5,7,8,3]
print(sol.peakElement(arr))