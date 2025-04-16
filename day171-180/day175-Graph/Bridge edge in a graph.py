from collections import defaultdict,deque
class Solution:
    # solucion usando DFS
    def isBridge(self, V, edges, c, d):
        # code here 
        adj=defaultdict(list)
        
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c):
                continue
            adj[u].append(v)
            adj[v].append(u)

        visited=[False]*V
        def is_connected(i):
            if i==d:
                return True
            visited[i]=True
            for j in adj[i]:
                if not visited[j]:
                    if is_connected(j):
                        return True
                    
            return False
        
        return not is_connected(c)
    
    # solucion usando BFS
    def isBridge2(self, V, edges, c, d):
        adj=defaultdict(list)
        
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c):
                continue
            adj[u].append(v)
            adj[v].append(u)     

        q=deque([c])
        visited=[False]*V
        while q:
            nodo=q.popleft()
            visited[nodo]=True
            if nodo==d:
                return False
            for i in adj[nodo]:
                if not visited[i]:
                    q.append(i)
        return True

    

# V=4
# edges=[[0,1],[1,2],[2,3]]
# c,d=1,2
V=5
edges=[[2,1],[2,0],[1,0],[0,3],[3,4]]
c,d=2,1
sol=Solution()
print(sol.isBridge(V,edges,c,d))
print(sol.isBridge2(V,edges,c,d))