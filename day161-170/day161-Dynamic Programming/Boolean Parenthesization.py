class Solution:
    def countWays(self, s):
        # code here
        n=len(s)
        # numero de formas en que la expresion entre 
        # indices i y j evalua a False o True (0 ó 1)
        dp=[[[0,0] for _ in range(n)] for _ in range(n)]
        
        for i in range(0,n,2):
            if s[i]=="T":
                dp[i][i][1]=1
            else:
                dp[i][i][0]=1

        for length in range(2,n,2):
            for start in range(0,n-length,2):
                # start start+length
                for k in range(start+1,start+length,2):
                    leftFalse,leftTrue=dp[start][k-1][0],dp[start][k-1][1]
                    rightFalse,rightTrue=dp[k+1][start+length][0],dp[k+1][start+length][1]
                    if s[k]=="&":
                        dp[start][start+length][1]+=leftTrue*rightTrue
                        dp[start][start+length][0]+=leftFalse*rightTrue+leftTrue*rightFalse+leftFalse*rightFalse
                    elif s[k]=="|":
                        dp[start][start+length][1]+=leftFalse*rightTrue+leftTrue*rightFalse+leftTrue*rightTrue
                        dp[start][start+length][0]+=leftFalse*rightFalse
                    elif s[k]=="^":
                        dp[start][start+length][1]+=leftFalse*rightTrue+leftTrue*rightFalse
                        dp[start][start+length][0]+=leftFalse*rightFalse+leftTrue*rightTrue
        return dp[0][n-1][1]

# s = "T|T"    
sol=Solution()
s = "T|F|T"
print(sol.countWays(s))


