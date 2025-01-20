class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        l,r,t,b=0,m-1,0,n-1
        res=[]
        while l<=r and t<=b:
            for i in range(l,r+1):
                res.append(mat[t][i])
            t+=1
            if t>b:
                break
            for i in range(t,b+1):
                res.append(mat[i][r])
            r-=1
            if l>r:
                break
            for i in range(r,l-1,-1):
                res.append(mat[b][i])
            b-=1
            if b<t:
                break            
            for i in range(b,t-1,-1):
                res.append(mat[i][l])
            l+=1
        return res
    
#mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
mat=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18]]
print(Solution().spirallyTraverse(mat))