class Solution:
    def floydWarshall(self, dist):
        #Code here
        n=len(dist)
        
        for k in range(n):
            for i in range(n):
                for j in range(n):  
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

        return dist


sol=Solution()
dist = [[0, 4, 108, 5, 108], [108, 0, 1, 108, 6], [2, 108, 0, 3, 108], [108, 108, 1, 0, 2], [1, 108, 108, 4, 0]]
print(sol.floydWarshall(dist))