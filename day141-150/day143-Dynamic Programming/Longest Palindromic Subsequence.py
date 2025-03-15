class Solution:

    def longestPalinSubseq(self, s):
        # code here
        n=len(s)
        dp=[[1 for _ in range(n)] for _ in range(n)]
        for width in range(1,n):
            for j in range(n-width):
                start,end=j,j+width
                if s[start]==s[end]:
                    dp[start][end]=2+(dp[start+1][end-1] if start+1<=end-1 else 0)
                else:
                    dp[start][end]=max(dp[start+1][end],dp[start][end-1])
        return dp[0][n-1]
            
s = "bbabcbcab"
sol=Solution()
print(sol.longestPalinSubseq(s))
