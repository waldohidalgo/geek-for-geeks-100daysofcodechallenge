class Solution:
    def kthMissing(self, arr, k):
        # code here
        n=len(arr)
        c=0
        for i in range(n):
            if arr[i]-c-1>=k:
                return c+k
            k-=arr[i]-c-1
            c=arr[i]
            
        return c+k

    def kthMissing2(self,arr,k):
        n=len(arr)
        for i in range(n):
            if arr[i]>=k+i+1:
                return k+i      
        return k+n

    def kthMissing3(self,arr,k):
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]-mid-1<k:
                l=mid+1
            else:
                r=mid-1
        return l+k

sol=Solution()
arr= [3, 5, 9, 10, 11, 12]
k=3
#print(sol.kthMissing(arr,k))
print(sol.kthMissing2(arr,k))
print(sol.kthMissing3(arr,k))

