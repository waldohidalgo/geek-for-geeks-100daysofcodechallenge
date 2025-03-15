class Solution:
    def longestStringChain(self, words):
        # Code here
        max_length = 1
        words.sort(key=len)
        dp={}
        for word in words:
            dp[word]=1
            for i in range(len(word)):
                pred=word[:i]+word[i+1:]
                if pred in dp:
                    dp[word]=max(dp[word],dp[pred]+1)
            max_length=max(max_length,dp[word])
        return max_length
    
sol=Solution()
arr= ["abcd", "dbqca"]
print(sol.longestStringChain(arr))