class Solution:
    def findMin(self, arr):
        #complete the function here
        n=len(arr)
        l,r=0,n-1
        if arr[l]<arr[r]:
            return arr[l]
        while l<r:
            mid=(l+r)//2
            if arr[mid]>arr[r]:
                l=mid+1
            else:
                r=mid
        return arr[l]

    
arr=[4, 2, 3]
print(Solution().findMin(arr))

