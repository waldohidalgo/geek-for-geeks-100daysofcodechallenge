class Solution:
    def minRepeats(self, s1, s2):
        # code here 
        s_repeated=s1
        n=len(s1)
        m=len(s2)
        while len(s_repeated)<m:
            s_repeated+=s1
        if s_repeated.find(s2)!=-1:
                return len(s_repeated)//n
        s_repeated+=s1
        if s_repeated.find(s2)!=-1:
                return len(s_repeated)//n
        return -1
        
sol=Solution()
s1 = "ab"
s2 = "cab"
print(sol.minRepeats(s1,s2))