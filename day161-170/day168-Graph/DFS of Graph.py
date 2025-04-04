class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        # callstack
        res=[]
        seen=set()
        def rec(adj,k):
            row=adj[k]
            if k in seen:
                return
            res.append(k)
            seen.add(k)
            for i in range(len(row)):
                rec(adj,row[i])
        rec(adj,0)
        return res
    
    def dfs2(self, adj):
        # code here
        # stack explicita
        res=[]
        seen=set()
        stack=[0]
        while stack:
            el=stack.pop()
            if el not in seen:
                row=adj[el]
                seen.add(el)
                res.append(el)
                while row:
                    stack.append(row.pop())
        return res

    
#adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
#adj=[[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
adj=[[4,5],[2],[1,5],[4],[0,3],[0,2]]
sol=Solution()
print(sol.dfs2(adj))


