class Solution:
    def _kmp(self,pat):
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
    def _search(self, pat, txt):
        # code here
        lps=self._kmp(pat)
        n,i=len(txt),0
        m,j=len(pat),0

        while i<n:
            if txt[i]==pat[j]:
                i+=1
                j+=1
            if j==m:
                return True 
            elif i<n and txt[i]!=pat[j]:
                if j==0:
                    i+=1
                else:
                    j=lps[j-1]
        return False
    def minRepeats(self, s1, s2):
        # code here 
        
        n=len(s1)
        m=len(s2)
        repeats=-(-m // n)
        s_repeated=s1*repeats

        if self._search(s2,s_repeated):
                return repeats
        s_repeated+=s1
        if self._search(s2,s_repeated):
                return repeats+1
        return -1
    

s1 = "ww"
s2 = "www" 
print(Solution().minRepeats(s1,s2))