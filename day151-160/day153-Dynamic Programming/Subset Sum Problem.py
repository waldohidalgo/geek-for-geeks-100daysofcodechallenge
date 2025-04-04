class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        k=sum
        n=len(arr)
        dp=[[False]*(k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                if arr[i-1]==j:
                    dp[i][j]=True
                elif arr[i-1]<j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        # for row in dp:
        #     print(row)
        return dp[n][k]
    
    def isSubsetSum2(self, arr, sum):
        # code here 
        k=sum
        n=len(arr)
        dp=[False]*(k+1)
        for i in range(1,n+1):
            for j in range(k,0,-1):
                if arr[i-1]==j:
                    dp[j]=True
                elif arr[i-1]<j:
                    dp[j]=dp[j-arr[i-1]] or dp[j]
        return dp[k]
    

sol=Solution()

#arr,sum=[3, 34, 4, 12, 5, 2],30
arr,sum= [1, 2, 3],6
print(sol.isSubsetSum(arr,sum))
print(sol.isSubsetSum2(arr,sum))