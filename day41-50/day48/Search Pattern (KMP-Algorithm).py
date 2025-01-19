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

    def search(self, pat, txt):
        # code here
        lps=self._kmp(pat)
        n,i=len(txt),0
        m,j=len(pat),0
        res=[]
        while i<n:
            if txt[i]==pat[j]:
                i+=1
                j+=1
            if j==m:
                res.append(i-j)
                j=lps[j-1]
            elif i<n and txt[i]!=pat[j]:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
        return res
    

sol=Solution()
txt = "aabaacaadaabaaba"
pat = "aaba"
print(sol.search(pat,txt))