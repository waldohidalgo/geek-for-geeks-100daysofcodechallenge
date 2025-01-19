class Solution:

    def _reverse(self,arr,low,high):
        while low<high:
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high-=1
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        factor=d%n
        if factor==0:
            return arr
        self._reverse(arr,0,factor-1)
        self._reverse(arr,factor,n-1)
        self._reverse(arr,0,n-1)
        return arr
    
sol=Solution()
arr=  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d=3
print(sol.rotateArr(arr,d))
    