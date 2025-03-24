class Solution:

    def matrixMultiplication(self, arr):
        # code here
        n=len(arr)
        if n<=2:
            return 0
        dp=[[float("inf")]*n for _ in range(n)]
        for i in range(1,n):
            dp[i][i]=0
        for i in range(1,n-1):
            for j in range(1,n-i):
                for k in range(j,j+i):
                    dp[j][j+i]=min(dp[j][j+i],
                                   dp[j][k]+
                                   dp[k+1][j+i]+
                                   arr[j-1]*arr[k]*arr[j+i])
        return dp[1][n-1]
    
sol=Solution()
arr=[1, 2, 3, 4, 3]
print(sol.matrixMultiplication(arr))

            


        