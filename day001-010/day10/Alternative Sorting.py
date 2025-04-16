import heapq

class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        i=0
        j=len(arr)-1
        res=[]
        while i<=j:
            if i==j:
                res.append(arr[i])
                break
            res.append(arr[j])
            res.append(arr[i])
            i+=1
            j-=1
        return res
    

sol=Solution()
arr=[]
print(sol.alternateSort(arr))