class Solution:
    def findMinOperation(self, mat):
        # code here
        n=len(mat)
        sum_row=[sum(mat[i]) for i in range(n)]
        sum_col=[sum(mat[i][j] for i in range(n)) for j in range(n)]
        max_sum=max(max(sum_row),max(sum_col))
        count=0
        for i in range(n):
            for j in range(n):
                min_row=max_sum-sum_row[i]
                min_col=max_sum-sum_col[j]
                min_val=min(min_row,min_col)
                if(min_val):
                    mat[i][j]=mat[i][j]+min_val
                    count+=min_val
                    sum_row[i]+=min_val
                    sum_col[j]+=min_val
                else:
                    continue
        return count
    def findMinOperation2(self,mat):
        n=len(mat)
        sum_row=[sum(mat[i]) for i in range(n)]
        sum_col=[sum(mat[i][j] for i in range(n)) for j in range(n)]
        max_sum=max(max(sum_row),max(sum_col))
        count=0       
        i,j=0,0
        while i<n and j<n:
            min_row=max_sum-sum_row[i]
            min_col=max_sum-sum_col[j]
            min_val=min(min_row,min_col) 
            if(min_val):
                mat[i][j]=mat[i][j]+min_val
                count+=min_val
                sum_row[i]+=min_val
                sum_col[j]+=min_val
            if(sum_row[i]==max_sum):
                i+=1
            if(sum_col[j]==max_sum):
                j+=1
        return count






sol=Solution()
mat= [[1, 2], [3, 4]]
#print(sol.findMinOperation(mat))
print(sol.findMinOperation2(mat))


