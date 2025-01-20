
class Solution:
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        n=len(mat)
        for i in range(n):
            row=mat[i]
            l,r=0,n-1
            while l<r:
                row[l],row[r]=row[r],row[l]
                l+=1
                r-=1

        for i in range(n):
            for j in range(i,n):
                if i<j:
                    mat[i][j],mat[j][i]= mat[j][i],mat[i][j]

#mat=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]      
mat=[[1, 2],[3, 4]]
sol=Solution()
sol.rotateby90(mat)
print(mat)                         