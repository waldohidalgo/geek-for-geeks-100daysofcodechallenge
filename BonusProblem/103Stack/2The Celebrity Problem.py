class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        candidate=0
        for i in range(n):
            if mat[candidate][i]==1:
                candidate=i
        
        for i in range(n):
            if i!=candidate:
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1
                
        return candidate
    
    def celebrity2(self, mat):
        n=len(mat)
        candidates=list(range(n))
        while len(candidates)>1:
            candidate_a=candidates.pop()
            candidate_b=candidates.pop()
            if mat[candidate_a][candidate_b]==1:
                candidates.append(candidate_b)
            else:
                candidates.append(candidate_a)
        candidate=candidates.pop()
        for i in range(n):
            if i!=candidate:
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1
                
        return candidate   
    
    def celebrity3(self, mat):
        # code here
        n=len(mat)
        i,j=0,n-1
        while i<j:
            if mat[i][j]==1:
                i+=1
            else:
                j-=1
        candidate=i

        for i in range(n):
            if i!=candidate:
                if mat[candidate][i]==1 or mat[i][candidate]==0:
                    return -1
                
        return candidate   



sol=Solution()
# arr= [[1, 1], [1, 1]]
arr=[[1, 1, 0], [0, 1, 0], [0, 1, 1]]
print(sol.celebrity(arr))
print(sol.celebrity2(arr))
print(sol.celebrity3(arr))

            
