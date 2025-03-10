class Solution:
    def lowerBound(self, arr, target):
        #code here
        n=len(arr)
        l,r=0,n-1
        if arr[r]<target:
            return n
        while l<r:
            mid=(l+r)//2
            if arr[mid]>=target:
                r=mid
            else:
                l=mid+1
        return l
    
arr=[2, 3, 7, 10, 11, 11, 25]
sol=Solution()
target=100
print(sol.lowerBound(arr,target))