class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        count_inc=0
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1] or arr[i]<arr[i-1]:
                count_inc+=arr[i-1]-arr[i]+1
                arr[i]=arr[i-1]+1
        return count_inc   
    
arr=[1, 2, 2]
print(Solution().minIncrements(arr))