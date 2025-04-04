class Solution:
    def minCoins(self, coins, sum):
        # code here
        if sum==0:
            return 0
        n=len(coins)
        k=sum
        dp=[[-1]*(k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                if coins[i-1]==j:
                    dp[i][j]= 1
                elif coins[i-1]<j:
                    if (dp[i-1][j]!=-1 and dp[i][j-coins[i-1]]!=-1):
                        dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                    elif dp[i-1][j]!=-1:
                        dp[i][j]=dp[i-1][j]
                    elif dp[i][j-coins[i-1]]!=-1:
                        dp[i][j]=1+dp[i][j-coins[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]

        # for row in dp:
        #     print(row)
        return dp[n][k]

    def minCoins2(self, coins, sum):
        # code here
        if sum==0:
            return 0
        n=len(coins)
        k=sum
        dp=[-1]*(k+1)
        for i in range(1,n+1):
            for j in range(1,k+1):
                if coins[i-1]==j:
                    dp[j]= 1
                elif coins[i-1]<j:
                    if dp[j]!=-1 and dp[j-coins[i-1]]!=-1:
                        dp[j]=min(dp[j],1+dp[j-coins[i-1]])
                    elif dp[j]!=-1:
                        dp[j]=dp[j]
                    elif dp[j-coins[i-1]]!=-1:
                        dp[j]=1+dp[j-coins[i-1]]
                    else:
                        dp[j]=-1
        # for row in dp:
        #     print(row)
        return dp[k]  

sol=Solution()
arr=[25, 10, 5]
sum=30
print(sol.minCoins(arr,sum))
print(sol.minCoins2(arr,sum))