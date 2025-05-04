import heapq
from collections import defaultdict

class Solution:
    def findMinCycle(self, V, edges):
        # code here
        def dijkstra(start, end, graph, deleted_badge):
            heap = [(0, start)]
            visited = set()
            while heap:
                dist, node = heapq.heappop(heap)
                # existe ciclo
                if node == end:
                    return dist
                # si el nodo ya fue visitado, se salta debido a que ya existe una 
                # distancia menor
                if node in visited:
                    continue
                visited.add(node)
                for neighbor, weight in graph[node]:
                    if (node, neighbor) == deleted_badge or (neighbor, node) == deleted_badge:
                        continue
                    if neighbor not in visited:
                        heapq.heappush(heap, (dist + weight, neighbor))

            # si no hay ciclo entre start y end      
            return float('inf')
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        min_cycle = float('inf')
        for u,v,w in edges:
                distance = dijkstra(u, v, graph, (u, v))
                min_cycle = min(min_cycle, distance + w)
        
        return min_cycle
    
# V = 5
# edges = [[0, 1, 2], [1, 2, 2], [1, 3, 1], [1, 4, 1], [0, 4, 3], [2, 3, 4]]
V = 5
edges = [[0, 1, 3], [1, 2, 2], [0, 4, 1], [1, 4, 2], [1, 3, 1], [3, 4, 2], [2, 3, 3]]
sol=Solution()
print(sol.findMinCycle(V,edges))