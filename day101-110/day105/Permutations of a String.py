class Solution:
    def findPermutation(self, s):
        # Code here
        res=set()
        def rec(s,word):
            n=len(s)
            if n==0:
                res.add(word)
                return
            for i in range(n):
                ch=s[i]
                rec(s[0:i]+s[i+1:],word+ch)
        rec(s,"")
        return list(res)
    
sol=Solution()
s="ABC"
print(sol.findPermutation(s))
print()


