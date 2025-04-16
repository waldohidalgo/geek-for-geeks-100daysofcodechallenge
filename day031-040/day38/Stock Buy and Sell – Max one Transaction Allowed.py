class Solution:
    def maximumProfit(self, prices):
        # code here
        n=len(prices)
        buy=True
        sell=False
        profit=0
        priceBuy=0

        for i in range(n-1):
            if prices[i]<prices[i+1] and buy==True:
                buy=False
                sell=True
                priceBuy=prices[i]
            elif prices[i]>prices[i+1] and sell==True:
                buy=True
                sell=False
                profit=max(profit,prices[i]-priceBuy)
        if sell==True and buy==False:
            profit=max(profit,prices[n-1]-priceBuy)
        
        return profit    
    
    def maximumProfit2(self, prices):
        n=len(prices)
        current_max=prices[-1]
        profit=0
        for i in range(n-2,-1,-1):
            current_max=max(current_max,prices[i+1])
            profit=max(profit,current_max-prices[i])
        return profit

    

sol=Solution()
arr= [7, 10, 1, 3, 6, 9, 2]
print(sol.maximumProfit(arr))
print(sol.maximumProfit2(arr))