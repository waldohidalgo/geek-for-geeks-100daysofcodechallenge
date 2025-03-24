class Solution:
    def countWays(self, digits):
        # Code here
        n=len(digits)
        if n<2:
            return 1 if digits[0]!="0" else 0
        dp=[1]*(n+1)
        dp[1]=1 if digits[0]!="0" else 0
        for i in range(2,n+1):
            if digits[i-1]=="0":
                dp[i]=dp[i-2] if (digits[i-2]=="1") or (digits[i-2]=="2") else 0
            else:
                val=10*int(digits[i-2])+int(digits[i-1])
                if val>9 and val<=26:
                    dp[i]=(dp[i-2]+dp[i-1])
                else:
                    dp[i]=dp[i-1]
        return dp[n]


    def countWays2(self, digits):
        # Code here
        n=len(digits)
        if n<2:
            return 1 if digits[0]!="0" else 0
        prev2=1
        prev1=1 if digits[0]!="0" else 0
        for i in range(2,n+1):
            if digits[i-1]=="0":
                curr=prev2 if (digits[i-2]=="1") or (digits[i-2]=="2") else 0
            else:
                val=10*int(digits[i-2])+int(digits[i-1])
                if val>9 and val<=26:
                    curr=(prev2+prev1)
                else:
                    curr=prev1
            prev2=prev1
            prev1=curr
        return curr
    

sol=Solution()
digits = "1615189843"
print(sol.countWays(digits))
print(sol.countWays2(digits))

