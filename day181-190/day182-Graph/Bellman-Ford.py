class Solution:
    # algoritmo de bellman ford
    def bellmanFord(self, V, edges, src):
        #code here
        INF = pow(10,8)
        dist = [INF] * V
        dist[src] = 0

        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]

        return dist

# V = 5
# edges= [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
# src = 0
V = 4
edges = [[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
src = 0
sol=Solution()
print(sol.bellmanFord(V,edges,src))