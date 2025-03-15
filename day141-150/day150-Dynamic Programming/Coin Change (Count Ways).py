class Solution:
    def count(self, coins, k):
        # code here 
        n=len(coins)
        dp=[[0]*(k+1) for _ in  range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                if coins[i-1]==j:
                    # monedas menores a coins[i-1] no forman ningun grupo, 
                    # solo forma grupo la moneda coins[i-1] con ella misma
                    dp[i][j]=dp[i-1][j]+1 
                elif coins[i-1]<j:
                    #los mismos i elementos para j-coins[i-1] monedas 
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]] 
                else:
                    dp[i][j]=dp[i-1][j]
        #print(dp)
        return dp[n][k]
    

    # optimizacion
    def count2(self, coins, k):
        # code here 
        n=len(coins)
        dp=[0]*(k+1)
        for i in range(1,n+1):
            for j in range(coins[i-1],k+1):
                if coins[i-1]==j:
                    # monedas menores a coins[i-1] no forman ningun grupo, 
                    # solo forma grupo la moneda coins[i-1] con ella misma
                    dp[j]=dp[j]+1 
                else:
                    # los mismos i elementos para j-coins[i-1] monedas 
                    dp[j]=dp[j]+dp[j-coins[i-1]] 
        #print(dp)
        return dp[k]

#coins,k=[2, 5, 3, 6],10

#coins,k= [1, 2, 3],4
coins,k=[5,10],10
print(Solution().count(coins,k))
print(Solution().count2(coins,k))