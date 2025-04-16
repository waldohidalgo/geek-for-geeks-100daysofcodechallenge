from collections import defaultdict
class Solution:
    # tarjan algorithm
    def articulationPoints(self, V, edges):
        # code here
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        discover = [-1] * V       # Tiempo de descubrimiento
        low = [-1] * V            # Tiempo más bajo alcanzable
        parent = [-1] * V         # Padre en el árbol DFS
        ap = [False] * V          # punto de articulación
        time = [0]                # Contador de tiempo mutable

        def dfs(u):
            children = 0
            discover[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if discover[v] == -1: 
                    parent[v] = u
                    children += 1
                    dfs(v)

                    # actualizacion de low[u] luego del recorrido
                    low[u] = min(low[u], low[v])
                    
                    # u no es raíz y low[v] >= discover[u]
                    if parent[u] != -1 and low[v] >= discover[u]:
                        ap[u] = True

                elif v != parent[u]:  # Back edge
                    low[u] = min(low[u], discover[v])

            # u es raíz y tiene >1 hijos
            if parent[u] == -1 and children > 1:
                ap[u] = True
       
        for i in range(V):
            if discover[i] == -1:
                dfs(i)
        
        print(low)
        result = [i for i, is_ap in enumerate(ap) if is_ap]
        return result if result else [-1]


sol=Solution()
# V = 5
# edges= [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
# V=4
# edges= [[0, 1], [0, 2]]
V=4
edges=[[0,1],[1,2],[2,3],[3,0],[3,1]]
print(sol.articulationPoints(V,edges))