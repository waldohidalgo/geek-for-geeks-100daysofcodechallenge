class Solution:
    def countSum(self, arr, target):
        #code here
        hs={}
        n=len(arr)
        ct=0
        for i in range(n):
            for p in range(i-1):
                curr=arr[p]+arr[i-1]  
                hs[curr]=hs.get(curr,0)+1  
            for j in range(i+1,n):
                ct+=hs.get(target-arr[i]-arr[j],0)

        return ct
    
# arr=[1, 5, 3, 1, 2, 10]
# target=20
arr=[1, 1, 1, 1, 1]
target=4
print(Solution().countSum(arr,target))