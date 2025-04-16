class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
        n,m=len(mat),len(mat[0])
        if(x<mat[0][0] or x>mat[n-1][m-1]):
            return False
        t,d=0,n-1
        row=-1
        while t<=d:
            mid=(t+d)//2
            if(mat[mid][0]<=x<=mat[mid][m-1]):
                row=mid
                break
            elif(mat[mid][0]>x):
                d=mid-1
            else:
                t=mid+1
        if row==-1:
            return False
        else:
            row_arr=mat[row]
            l,r=0,m-1
            while l<=r:
                mid=(l+r)//2
                if(row_arr[mid]==x):
                    return True
                elif(row_arr[mid]<x):
                    l=mid+1
                else:
                    r=mid-1
            return False

sol=Solution()
arr= [[87, 96, 99], [101, 103, 111]]
x=111
print(sol.searchMatrix(arr,x))    



        
