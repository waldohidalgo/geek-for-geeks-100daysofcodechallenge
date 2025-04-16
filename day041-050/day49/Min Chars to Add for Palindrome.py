class Solution:
    def _kmp(self, pat):
        n=len(pat)
        lps=[0]*n
        i=1
        j=0
        while i<n:
            if pat[i]==pat[j]:
                lps[i]=j+1
                i+=1
                j+=1
            elif j==0:
                lps[i]=0
                i+=1
            else:
                j=lps[j-1]
        return lps        
    def minChar(self, s):
        #Write your code here
        lps=self._kmp(s+"$"+s[::-1])
        return len(s)-lps[-1]

    
s = "aacecaaaa"

sol=Solution()
print(sol.minChar(s))