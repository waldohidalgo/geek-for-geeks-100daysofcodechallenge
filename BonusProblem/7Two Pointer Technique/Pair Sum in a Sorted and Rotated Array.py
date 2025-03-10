class Solution:
    ##Complete this function
    def pairInSortedRotated(self,arr, target):
        #Your code here
        n=len(arr)
        # if arr[0]>=arr[n-1]:
        #     l=1
        #     while l<n-1 and arr[l]>=arr[l-1]:
        #         l+=1
        #     r=l-1
        # else:
        #     l,r=0,n-1
        l,r=0,n-1
        while l<r:
            mid=(l+r)//2
            if arr[mid]>arr[r]:
                l=mid+1
            elif arr[mid]==arr[r]:
                r-=1
            else:
                r=mid
        r=(l-1+n)%n
        while l!=r:
            acc=arr[l]+arr[r]
            if acc>target:
                r=(r-1+n)%n
            elif acc<target:
                l=(l+1)%n
            else:
                return True
        return False

sol=Solution()
arr=[3,2,2,2,2,2,2]
target=5
#arr=[1,5,7,9,1,1,1]
#target=16
print(sol.pairInSortedRotated(arr,target))