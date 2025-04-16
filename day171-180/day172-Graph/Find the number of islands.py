
class Solution:
    # solucion usando DFS
    def numIslands(self, grid):
        # code here
        n,m=len(grid),len(grid[0])
        visited=[[False]*m for _ in range(n)]
        directions=[(-1,-1),(-1,0),
                    (-1,1),(0,-1),
                    (0,1),(1,-1),
                    (1,0),(1,1)]
        def dfs(i,j):
            if visited[i][j]:
                return
            
            visited[i][j]=True
            for dx,dy in directions:
                if 0<=i+dx<n and 0<=j+dy<m and grid[i+dx][j+dy]=="L":
                    dfs(i+dx,j+dy)

        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="L" and not visited[i][j]:
                    dfs(i,j)
                    count+=1
        return count
    
    def numIslands2(self,grid):
        from collections import deque
        n,m=len(grid),len(grid[0])
        visited=[[False]*m for _ in range(n)]
        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        def bfs(i,j):
            q=deque([(i,j)])
            while q:
                i,j=q.popleft()
                visited[i][j]=True
                for dx,dy in directions:
                    if 0<=i+dx<n and 0<=j+dy<m and grid[i+dx][j+dy]=="L" and not visited[i+dx][j+dy]:
                        q.append((i+dx,j+dy))
                        

        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="L" and not visited[i][j]:
                    bfs(i,j)
                    count+=1
        return count 

sol=Solution()
grid = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]

#grid=[['W', 'L', 'L', 'L', 'W', 'W', 'W'], ['W', 'W', 'L', 'L', 'W', 'L', 'W']]
print(sol.numIslands(grid))
print(sol.numIslands2(grid))