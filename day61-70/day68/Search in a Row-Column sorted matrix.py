class Solution:
    def matSearch(self, mat, x):
        # Complete this function
        n,m=len(mat),len(mat[0])
        t,r=0,m-1
		
        while t<n and r>=0:
            current=mat[t][r]
            if current==x:
                return True
            if current>x:
                r=r-1
            else:
                t=t+1
        return False

sol=Solution()
mat=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
x=10
print(sol.matSearch(mat,x))
			
		