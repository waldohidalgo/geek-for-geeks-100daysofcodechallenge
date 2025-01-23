class Solution:
    def _kmp(self,pat):
        n=len(pat)
        lps=[0]*n
        i=1
        j=0
        while i<n:
            if pat[i]==pat[j]:
                j+=1
                lps[i]=j
                i+=1
            elif j==0:
                lps[i]=0
                i+=1
            else:
                j=lps[j-1]
        return lps
        
    def longestPrefixSuffix(self, s):
		# code here
        lps=self._kmp(s)
        return lps[-1]
    
s = "aaaa"
sol = Solution()
print(sol.longestPrefixSuffix(s))