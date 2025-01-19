class Solution:
    def search(self,arr,key):
        # Complete this function
        n=len(arr)
        l,r=0,n-1
        while l<=r:  
            #print(l,r)      
            if l==r and arr[l]!=key:
                return -1            
            mid=(l+r)//2
            if arr[mid]==key:
                return mid

            if arr[mid]>arr[r]:
                if key>=arr[l] and key<arr[mid]:
                    r=mid
                else:
                    l=mid+1
            else:
                if key>arr[mid] and key<=arr[r]:
                    l=mid+1
                else:
                    r=mid

    def search2(self,arr,key):
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            if l==r and arr[l]!=key:
                return -1             
            mid=(l+r)//2
            if arr[mid]==key:
                return mid
            if arr[l]<=arr[mid]:
                if arr[l]<=key and key<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<key and key<=arr[r]:
                    l=mid+1
                else:
                    r=mid-1


# arr= [5,6,7,8,9,10,1,2,3]
# key=10
# arr=[5, 6, 7, 8, 9, 10, 1, 2, 3]
# key = 7
arr=[3,5,1,2]
key=6
# for i in arr:
#     print(Solution().search(arr,i))
print(Solution().search(arr,key))