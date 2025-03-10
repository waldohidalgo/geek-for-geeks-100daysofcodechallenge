from typing import List

class Solution:
    def zeroSumSubmat(self, mat):
        # code here
        n,m=len(mat),len(mat[0]) # n rows, m columns
        max_length=0
        for i in range(n):
            arr=[0]*m
            for j in range(i,n):
                for k in range(m):
                    arr[k]=arr[k]+mat[j][k]
                hs={0:-1}
                acc=0
                for k in range(m):
                    acc+=arr[k]
                    if acc in hs:
                        max_length=max(max_length,(j-i+1)*(k-hs[acc]))
                    if acc not in hs:
                        hs[acc]=k  
        return max_length              
                
mat= [[1, -1], [-1, 1]]
sol=Solution()
print(sol.zeroSumSubmat(mat))