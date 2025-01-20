#from collections import defaultdict
class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        res={}
        for e in a:
            res[e]=res.get(e,0) 
        for e in b:
            val=res.get(e,-1)
            if val!=-1:
                res[e]=1 if val==0 else val
        return [k for k,v in res.items() if v==1]
                


    
sol=Solution()
#a=[1, 2, 1, 3, 1]
#b=[3, 1, 3, 4, 1]
a=[1,1,1]
b=[1, 1, 1, 1, 1]
print(sol.intersectionWithDuplicates(a,b))
