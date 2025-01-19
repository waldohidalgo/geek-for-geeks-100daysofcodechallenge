class Solution:
    def _reverse(self,arr,low,high):
        while low<high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        i=n-2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i==-1:
            self._reverse(arr,0,n-1)
            return arr
        j=n-1
        while arr[j]<=arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
        self._reverse(arr,i+1,n-1)
        return arr
    
sol=Solution()
arr=[3,2,1]
print(sol.nextPermutation(arr))
print(arr)