class Solution:
	def rotateMatrix(self, mat):
		# Code here
		n=len(mat)
		for i in range(n):
			l,r=0,n-1
			while l<r:
				mat[i][l],mat[i][r]=mat[i][r],mat[i][l]
				l+=1
				r-=1
		for j in range(n):
			t,d=0,n-1
			while t<d:
				mat[t][j],mat[d][j]=mat[d][j],mat[t][j]
				t+=1
				d-=1
				
sol=Solution()
mat=[[1, 2, 3, 4], 
                 [5, 6, 7 ,8], 
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]]
sol.rotateMatrix(mat)
print(mat)