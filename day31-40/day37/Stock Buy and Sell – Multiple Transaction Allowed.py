from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
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
                profit+=prices[i]-priceBuy
        if sell==True and buy==False:
            profit+=prices[n-1]-priceBuy
        
        return profit

sol=Solution()
#arr= [100, 180, 260, 310, 40, 535, 695]
#arr=  [4, 2, 2, 2, 4]
arr=[4,3,2,1]
print(sol.maximumProfit(arr))
                