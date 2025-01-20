class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        seen={}
        seen[arr[0]]=1
        n=len(arr)
        count=0
        for i in range(1,n):
            current=arr[i]
            count+=seen.get(target-current,0)
            seen[current]=seen.get(current,0)+1
        return count
    
sol=Solution()
arr= [1, 5, 7, -1, 5]
target=6
print(sol.countPairs(arr,target))