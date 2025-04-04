from collections import deque
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        res=[]
        visited=set()
        q=deque([0])
        while q:
            el=q.popleft()
            if el not in visited:
                res.append(el)
                visited.add(el)
                row=adj[el]
                for i in row:
                    if i not in visited:
                        q.append(i)
        return res
    
sol=Solution()
adj=[[2, 3, 1], [0], [0, 4], [0], [2]]
#adj=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print(sol.bfs(adj))
