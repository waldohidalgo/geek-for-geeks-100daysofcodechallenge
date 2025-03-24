class Solution:
    def maxProfit(self, prices, k):
        # code here
        n=len(prices)
        if k>=n//2:
            # se demuestra por induccion
            return sum(max(prices[i+1]-prices[i],0) for i in range(n-1))
        
        # dp[i][j] cantidad maxima de beneficio obtenida
        # realizando i transacciones hasta el día j
        dp=[[0]*(n+1) for _ in range(k+1)]

        for i in range(1,k+1):
            max_prev=float('-inf')
            for j in range(1,n+1):
                dp[i][j]=max(dp[i][j-1],prices[j-1]+max_prev)
                max_prev=max(max_prev,dp[i-1][j]-prices[j-1])
        return dp[k][n]
    

    def maxProfit2(self, prices, k):
        # code here
        n=len(prices)
        if k>=n//2:
            # se demuestra por induccion
            return sum(max(prices[i+1]-prices[i],0) for i in range(n-1))
        
        # dp[i][j] cantidad maxima de beneficio obtenida
        # realizando i transacciones hasta el día j
        dp=[0]*(n+1)

        for i in range(1,k+1):
            max_prev=float('-inf')
            for j in range(1,n+1):
                prev=dp[j]
                dp[j]=max(dp[j-1],prices[j-1]+max_prev)
                max_prev=max(max_prev,prev-prices[j-1])
        return dp[n]

prices= [10,22,5,75,65,80]
k = 2
sol=Solution()
print(sol.maxProfit(prices,k))
print(sol.maxProfit2(prices,k))