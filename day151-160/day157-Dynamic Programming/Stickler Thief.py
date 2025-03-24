class Solution:  
    def findMaxSum(self,arr):
        # code here
        n=len(arr)
        if n<3:
            return max(arr)
        dp=[0]*(n+1)
        dp[1]=arr[0]
        dp[2]=max(arr[0],arr[1])
        for i in range(3,n+1):
            dp[i]=max(dp[i-1],arr[i-1]+dp[i-2])

        return dp[n]
    
    def findMaxSum2(self,arr):
        # code here
        n=len(arr)
        if n<3:
            return max(arr)
        prev2=arr[0]
        prev1=max(arr[0],arr[1])
        for i in range(3,n+1):
            curr=max(prev1,arr[i-1]+prev2)
            prev2=prev1
            prev1=curr

        return curr

arr=[8, 5,12]
sol=Solution()
print(sol.findMaxSum(arr))
print(sol.findMaxSum2(arr))