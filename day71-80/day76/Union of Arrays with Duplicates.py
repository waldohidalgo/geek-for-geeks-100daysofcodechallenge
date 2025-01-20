class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # code here
        res=set(a)

        for e in b:
            if e not in res:
                res.add(e)
        return len(res)

sol=Solution()
a=[1,2,3]
b= [4,5,6] 
print(sol.findUnion(a,b))