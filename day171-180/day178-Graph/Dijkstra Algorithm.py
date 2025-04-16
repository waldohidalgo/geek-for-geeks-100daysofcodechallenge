import heapq
from collections import defaultdict
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        dist = [float('inf')] * V
        dist[src] = 0
        heap = [(0, src)]

        while heap:
            curr_distance,nodo=heapq.heappop(heap)

            if curr_distance>dist[nodo]:
                continue

            for i,w in adj[nodo]:
                if dist[nodo]+w<dist[i]:
                    dist[i]=dist[nodo]+w
                    heapq.heappush(heap,(dist[i],i))
        return dist

# V = 3 
# edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
# src = 2
V = 5
edges= [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]]
src = 0
sol=Solution()
print(sol.dijkstra(V,edges,src))