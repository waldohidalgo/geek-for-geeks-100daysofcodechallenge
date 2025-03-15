class Solution:
    def knapsack(self, W, val, wt):
        # code here
        n=len(val)
        # dp[i][j] cantidad máxima de suma de valores considerando los primeros
        # i elementos con un limite de peso máximo igual a j
        dp=[[0]*(W+1) for _ in range(n+1)]
        for i in range(1,n+1): 
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        print(dp)
        return dp[n][W]

    def knapsack2(self, W, val, wt):
        # code here
        n=len(val)
        # dp[i][j] cantidad máxima de suma de valores considerando los primeros
        # i elementos con un limite de peso máximo igual a j
        dp=[0]*(W+1)
        for i in range(1,n+1): 
            for j in range(W,wt[i-1]-1,-1):
                dp[j]=max(dp[j],val[i-1]+dp[j-wt[i-1]])
        print(dp)
        return dp[W]


sol=Solution()
# W = 3
# val = [1, 2, 3]
# wt = [4, 5, 6] 
# W = 5
# val = [10, 40, 30, 50]
# wt = [5, 4, 2, 3] 
W = 7
val = [10,8,6]
wt = [1,7,9]
print(sol.knapsack(W,val,wt))
print(sol.knapsack2(W,val,wt))       

