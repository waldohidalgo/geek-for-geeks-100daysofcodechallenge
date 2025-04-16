from collections import defaultdict,deque
class Solution:
    def isCycle(self, V, edges):
        # code here
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)

    
        def is_cycle(j,visited):
            row=adj[j]
            for i in row:
                if i not in visited:
                    visited.add(i)
                    if is_cycle(i,visited):
                        return True
                    visited.remove(i)
                else:
                    return True
            return False

        for i in range(V):
            visited=set()
            visited.add(i)
            if is_cycle(i,visited):
                    return True
        return False

    def isCycle2(self,V,edges):
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)    

        visited=[False]*V
        visited_rec=[False]*V

        def is_cycle(j):
            visited[j]=True
            visited_rec[j]=True
            row=adj[j]
            for i in row:
                if not visited[i]:
                    if is_cycle(i):
                        return True
                elif visited_rec[i]:
                    return True
            visited_rec[j]=False    
            return False


        for i in range(V):
            if not visited[i]:
                if is_cycle(i):
                        return True
        return False
    
    # uso de algoritmo de Kahn
    def isCycle3(self,V,edges):
        adj=defaultdict(list)
        in_degree=[0]*V
        for u,v in edges:
            adj[u].append(v) 
            in_degree[v]+=1    
        queue = deque(i for i in range(V) if in_degree[i] == 0)    
        count=0
        while queue:
            node = queue.popleft()
            count += 1

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return count!=V
# V = 4
# edges= [[0, 1], [1, 2], [2, 3], [3, 3]]
# V=3
# edges= [[0, 1], [1, 2],[2,0]]
# V=5
# edges=[[3,0],[4,2],[1,2]]
# V=4
# edges=[[0,3],[0,1],[1,3]]
V=5
edges=[[0,3],[0,1],[1,3],[3,4],[1,4]]

sol=Solution()
print(sol.isCycle(V,edges))
print(sol.isCycle2(V,edges))
print(sol.isCycle3(V,edges))