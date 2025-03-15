class Solution:

    def countPS(self, s):
        # code here
        n=len(s)
        dp=[[True for _ in range(n)] for _ in range(n)]
        ct=0
        for width in range(1,n):
            for j in range(n-width):
                start,end=j,j+width
                if s[start]==s[end] and (dp[start+1][end-1] if (width+1)>2 else True):
                    ct+=1
                else:
                    dp[start][end]=False

        return ct
    
sol=Solution()
s = "abbaeae"
#s ="aaa"
print(sol.countPS(s))