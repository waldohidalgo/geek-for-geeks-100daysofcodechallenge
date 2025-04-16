class Solution:
    def floodFill(self, image, sr, sc, newColor):
        #Code here
        color=image[sr][sc]
        if color==newColor:
            return image
        n,m=len(image),len(image[0])

        visited=[[False]*m for _ in range(n)]

        directions=[(0,-1),(1,0),(0,1),(-1,0)]
        

        def dfs(i,j):
            if visited[i][j]:
                return
            visited[i][j]=True
            image[i][j]=newColor
            for dx,dy in directions:
                if 0<=i+dx<n and 0<=j+dy<m and image[i+dx][j+dy]==color:
                    dfs(i+dx,j+dy)
 
        dfs(sr,sc)
        return image
    
    def floodFill2(self, image, sr, sc, newColor):
        from collections import deque
        color=image[sr][sc]

        if color==newColor:
            return image
        
        n,m=len(image),len(image[0])

        visited=[[False]*m for _ in range(n)]

        directions=[(0,-1),(1,0),(0,1),(-1,0)]
        
        q=deque([(sr,sc)])
        while q:
            i,j=q.popleft()
            visited[i][j]=True
            image[i][j]=newColor
            for dx,dy in directions:
                if 0<=i+dx<n and 0<=j+dy<m and image[i+dx][j+dy]==color and not visited[i+dx][j+dy]:
                    q.append((i+dx,j+dy))
        return image





sol=Solution()
# image = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
# sr = 1
# sc = 2
# newColor = 2
# image= [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
# sr = 1
# sc = 1
# newColor = 2

image = [[0, 1, 0], [0, 1, 0]]
sr = 0
sc = 1
newColor = 0
print(sol.floodFill2(image,sr,sc,newColor))
                