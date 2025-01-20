class Solution:



    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
        def searchInRow(row,x,n):
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if row[mid]==x:
                    return True
                if row[mid]>=x:
                    r=mid-1
                else:
                    l=mid+1
            return False
        
        m,n=len(mat),len(mat[0])
        for k in range(m):
            row=mat[k]
            if searchInRow(row,x,n):
                return True
        return False
    

sol=Solution()
mat=[[1, 2, 9],[65, 69, 75]]
x=99
print(sol.searchRowMatrix(mat,x))
