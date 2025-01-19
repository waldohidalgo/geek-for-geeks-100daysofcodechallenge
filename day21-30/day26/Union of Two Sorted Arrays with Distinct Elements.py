class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        i=0
        j=0
        res=[]
        while i<len(a) and j<len(b):
            if a[i]==b[j]:
                res.append(a[i])
                i+=1
                j+=1
            elif a[i]<b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        while i<len(a):
            res.append(a[i])
            i+=1
        while j<len(b):
            res.append(b[j])
            j+=1
        return res

sol=Solution()
a= [1,5]
b = [2]
print(sol.findUnion(a,b))