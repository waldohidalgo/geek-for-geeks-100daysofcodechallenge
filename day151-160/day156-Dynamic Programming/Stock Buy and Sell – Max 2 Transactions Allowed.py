class Solution:
    def maxProfit(self, prices):
        # code here
        n=len(prices)
        # cantidad maxima de beneficio con un maximo de i
        # transacciones para el día j
        dp=[[0]*(n+1) for _ in range(2+1)]
        for i in range(1,3):
            max_prev_buy1=float("-inf")
            max_prev_buy2=float("-inf")
            for j in range(1,n+1):
                if i==1:
                    dp[i][j]=max(dp[i][j-1],prices[j-1]+max_prev_buy1)
                    max_prev_buy1=max(max_prev_buy1,-prices[j-1])
                else:
                    dp[i][j]=max(dp[i][j-1],prices[j-1]+max_prev_buy2)
                    max_prev_buy2=max(max_prev_buy2,-prices[j-1]+dp[i-1][j])

        return dp[2][n]
    

    def maxProfit2(self, prices):
        # code here
        n=len(prices)
        # cantidad maxima de beneficio con un maximo de i
        # transacciones para el día j
        dp=[0]*(n+1)
        for i in range(1,3):
            max_prev_buy1=float("-inf")
            max_prev_buy2=float("-inf")
            for j in range(1,n+1):
                prev_profit=dp[j]
                if i==1:
                    dp[j]=max(dp[j-1],prices[j-1]+max_prev_buy1)
                    max_prev_buy1=max(max_prev_buy1,-prices[j-1])
                else:
                    dp[j]=max(dp[j-1],prices[j-1]+max_prev_buy2)
                    max_prev_buy2=max(max_prev_buy2,-prices[j-1]+prev_profit)

        return dp[n]
    
#prices=[2, 30, 15, 10, 8, 25, 80]
prices=[10, 22, 5, 75, 65, 80]
sol=Solution()
print(sol.maxProfit(prices))
print(sol.maxProfit2(prices))