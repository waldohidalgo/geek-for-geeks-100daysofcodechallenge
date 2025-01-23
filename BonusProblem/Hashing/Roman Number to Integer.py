class Solution:
    def romanToDecimal(self, s): 
        # code here
        values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        n=len(s)
        for i in range(n):
            curr=values[s[i]]
            nv=values[s[i+1]] if i<n-1 else float('-inf')
            if curr<nv:
                res-=curr
            else:
                res+=curr
        return res
s= 'IX'
print(Solution().romanToDecimal(s))