
class Solution:
    def isCycle(self, V, edges):
        #Code here
        adj = {}
        for u, v in edges:
            if u not in adj:
                adj[u]=[v]
            else:
                adj[u].append(v)
            if v not in adj:
                adj[v]=[u]
            else:
                adj[v].append(u)

        visited=set()
        def exist_cycle(curr_node,parent,visited,adj):
            visited.add(curr_node)
            row=adj[curr_node]
            for node in row:
                if node not in visited:
                    if exist_cycle(node,curr_node,visited,adj):
                        return True
                # conexion con nodo visitado distinto del padre implica ciclo
                elif node!=parent:
                    return True
            return False


        for node in range(V):
            if node not in visited:
                if exist_cycle(node,None,visited,adj):
                    return True
        return False        	
    
V = 6
edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[2,5]]
sol=Solution()
print(sol.isCycle(V,edges))