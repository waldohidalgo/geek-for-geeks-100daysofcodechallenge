class Solution:
    def removeDuplicates(self, arr):
        # code here 
        val=[None]*101
        for i in range(len(arr)):
            if val[arr[i]]==None:
                val[arr[i]]=1
            else:
                arr[i]=None
        return [i for i in arr if i!=None]
    
sol=Solution()
arr=[8, 7] 
print(sol.removeDuplicates(arr))