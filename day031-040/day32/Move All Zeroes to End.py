class Solution:
    def pushZerosToEnd(self,arr):
    	# code here
        n=len(arr)
        count=0
        for i in range(n):
            if arr[i]==0:
                count+=1
            else:
                arr[i-count]=arr[i]
        for i in range(count):
            arr[n-count+i]=0
        return arr

sol=Solution()
arr= [1, 2, 0, 4, 3, 0, 5, 0]
print(sol.pushZerosToEnd(arr))