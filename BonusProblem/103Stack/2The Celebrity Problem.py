class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        stack=[]
        for i in range(n):
            stack.append(i)
            for j in range(n):
                if i!=j:
                    if stack and mat[i][j]==1:
                        stack.pop()
                    if stack and mat[i][j]==0:
                        stack.pop()
        return stack
    
sol=Solution()
arr=[[1]]
print(sol.celebrity(arr))

            
