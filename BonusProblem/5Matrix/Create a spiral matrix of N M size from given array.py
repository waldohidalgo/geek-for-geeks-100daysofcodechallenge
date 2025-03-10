class Solution:
    def spiralFill(self, n, m, arr):
        # code here
        mat=[[0]*m for _ in range(n)]
        t,d,l,r=0,n-1,0,m-1
        p=0
        while p<n*m:
            for i in range(l,r+1):
                mat[t][i]=arr[p]
                p+=1
            t+=1
            if p<n*m:
                for i in range(t,d+1):
                    mat[i][r]=arr[p]
                    p+=1
                r-=1
            if p<n*m:
                for i in range(r,l-1,-1):
                    mat[d][i]=arr[p]
                    p+=1
                d-=1
            if p<n*m:
                for i in range(d,t-1,-1):
                    mat[i][l]=arr[p]
                    p+=1
                l+=1
        return mat
    
sol=Solution()
arr=[1,2,3,4]
n,m=4,1
print(sol.spiralFill(n,m,arr))