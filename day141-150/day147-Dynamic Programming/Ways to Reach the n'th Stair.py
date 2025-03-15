class Solution:
    def countWays(self, n):
        # code here
        dp=[1]*(n+1)
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
    def countWays2(self, n):
        # code here
        prev_one=1
        prev_two=1
        curr=1
        for i in range(2,n+1):
            curr=prev_one+prev_two
            prev_two=prev_one
            prev_one=curr
        return curr 
    
sol=Solution()
n=1
print(sol.countWays(n))
print(sol.countWays2(n))



