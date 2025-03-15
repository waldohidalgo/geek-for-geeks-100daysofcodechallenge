class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        n=len(cost)
        dp=[0]*(n+1)

        for i in range(2,n+1):
            dp[i]=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        return dp[n]
    
    def minCostClimbingStairs2(self, cost):
        #Write your code here
        n=len(cost)
        
        prev_one,prev_two=0,0
        curr=0
        for i in range(2,n+1):
            curr=min(prev_one+cost[i-1],prev_two+cost[i-2])
            prev_two=prev_one
            prev_one=curr
        return curr
    



cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sol=Solution()
print(sol.minCostClimbingStairs(cost))
print(sol.minCostClimbingStairs2(cost))