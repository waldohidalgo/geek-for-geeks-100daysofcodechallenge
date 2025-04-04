class Solution:
    def wordBreak(self, s, dictionary):
        # code here
        n=len(s)

        dp=[False]*(n+1)
        dp[0]=True
        
        for i in range(1,n+1):
            for word in dictionary:
                j=i-len(word)
                if j>=0 and dp[j] and s[j:i]==word:
                    dp[i]=True
                    break
        return dp[n]
    
s = "ilikemangoes"
dictionary = ["i", "like", "man", "india", "gfg","goeds"]
sol=Solution()
print(sol.wordBreak(s,dictionary))
