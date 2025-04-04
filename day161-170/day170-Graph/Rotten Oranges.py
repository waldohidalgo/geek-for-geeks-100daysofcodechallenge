from collections import deque

class Solution:
    def orangesRotting(self, mat):
        #Code here
        n=len(mat)
        m=len(mat[0])
        q=deque()
        count_1=0
        for i in range(n):
            for j in range(m):
                val=mat[i][j]
                if val==1:
                    count_1+=1
                elif val==2:
                    q.append((i,j))
        if count_1==0:
            return 0
        time=0
        while count_1>0 and q:
            length_q=len(q)
            for _ in range(length_q):
                i,j=q.popleft()
                if i-1>=0 and mat[i-1][j]==1:
                    count_1-=1
                    mat[i-1][j]=2
                    q.append((i-1,j))
                if i+1<n and mat[i+1][j]==1:
                    count_1-=1
                    mat[i+1][j]=2
                    q.append((i+1,j))
                if j-1>=0 and mat[i][j-1]==1:
                    count_1-=1
                    mat[i][j-1]=2
                    q.append((i,j-1))
                if j+1<m and mat[i][j+1]==1:
                    count_1-=1
                    mat[i][j+1]=2
                    q.append((i,j+1))
            time+=1
        if count_1:
            return -1
        else:
            return time
        
sol=Solution()
#mat=[[0, 1, 2], [0, 1, 2], [2, 1, 1]]
#mat=[[2, 2, 0, 1]]
mat=[[2, 1, 1], [0, 2, 0]]
print(sol.orangesRotting(mat))
        

		
		
				
		