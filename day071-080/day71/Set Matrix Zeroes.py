class Solution:
    def setMatrixZeroes(self, mat):
        n,m=len(mat),len(mat[0])
        haveZeroFirstRow=any(elem==0 for elem in mat[0] )
        haveZeroFirstColumn=any(mat[i][0]==0 for i in range(n))

        for j in range(1,m):
            for i in range(1,n):
                if mat[i][j]==0:
                    mat[0][j]=0
                    break

        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j]==0:
                    mat[i][0]=0
                    break

        for j in range(1,m):
            if mat[0][j]==0:
                for i in range(1,n):
                    mat[i][j]=0

        for i in range(1,n):
            if mat[i][0]==0:
                for j in range(1,m):
                    mat[i][j]=0

        if haveZeroFirstRow:
            for j in range(m):
                mat[0][j]=0
        if haveZeroFirstColumn:
            for i in range(n):
                mat[i][0]=0
        print(haveZeroFirstRow,haveZeroFirstColumn)

sol=Solution()
mat=[[1, -1, 1],
                [-1, 0, 1],
                [1, -1, 1]]
sol.setMatrixZeroes(mat=mat)
print(mat)