class Solution:
    def mergeSort(self,arr,low,high):
        count_inversion=0
        if low<high:
            mid=(low+high)//2
            count_inversion+=self.mergeSort(arr,low,mid)
            count_inversion+=self.mergeSort(arr,mid+1,high)
            count_inversion+=self.merge(arr,low,mid,high)
        return count_inversion    
    def merge(self,arr,low,mid,high):
        count_inversion=0
        temp=[0]*(high-low+1)
        i=low
        j=mid+1
        k=0
        while i<=mid and j<=high:
            if arr[i]<=arr[j]:
                temp[k]=arr[i]
                k+=1
                i+=1
            else:
                temp[k]=arr[j]
                k+=1
                j+=1
                count_inversion+=mid-i+1
        while i<=mid:
            temp[k]=arr[i]
            k+=1
            i+=1
        while j<=high:
            temp[k]=arr[j]
            k+=1
            j+=1
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        return count_inversion
        
    def inversionCount(self, arr):
        # Your Code Here
        n=len(arr)
        return self.mergeSort(arr,0,n-1)
    
arr= [5,4,3,2,1]
sol=Solution()
print(sol.inversionCount(arr))