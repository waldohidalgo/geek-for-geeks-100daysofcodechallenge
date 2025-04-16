class Solution:
    
    # implementacion con depth first search
    def topoSort(self, V, edges):
        # Code here
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u]=[v]
            else:
                adj[u].append(v)

        visited=[False]*V
        res=[]

        def dfs(j):
            if visited[j]:
                return
            visited[j]=True
            row=adj[j] if j in adj else []
            for node in row:
                dfs(node)
            res.append(j)


        for i in range(V):
            if not visited[i]:
                dfs(i)
        return res[::-1]
    


    # algoritmo de Kahn
    def topoSort2(self,V,edges):
        from collections import defaultdict,deque
        adj=defaultdict(list)
        in_degree=[0]*V
        for u,v in edges:
            adj[u].append(v)
            in_degree[v]+=1

        q=deque(nodo for nodo in range(V) if in_degree[nodo]==0)
        res=[]
 
        while q:
            nodo=q.popleft()
            res.append(nodo)
            row=adj[nodo]
            for i in row:
                in_degree[i]-=1
                if in_degree[i]==0:
                    q.append(i)

        return res


sol=Solution()
# V=4
# edges= [[3, 0], [1, 0], [2, 0]]
V=6
edges=[[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]
print(sol.topoSort2(V,edges))