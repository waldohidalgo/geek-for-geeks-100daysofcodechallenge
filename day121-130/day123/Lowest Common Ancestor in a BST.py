from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def _build(self,arr):
        n=len(arr)
        root=Node(arr[0])
        queue=deque([root])
        i=0
        while i<n:
            curr_root=queue.popleft()
            i+=1
            if i<n and arr[i]:
                left=Node(arr[i])
                curr_root.left=left
                queue.append(left)
            i+=1
            if i<n and arr[i]:            
                right=Node(arr[i])
                curr_root.right=right
                queue.append(right)

        return root 
    
    def _search_node(self,root,val):
        if not root or val==root.data:
            return root
        if val>root.data:
            node=self._search_node(root.right,val)
        else:
            node=self._search_node(root.left,val)
        return node
        
    def LCA(self, root, n1, n2):
        # your code here

        def rec(root):
            if n1.data<=root.data<=n2.data or n1.data>=root.data>=n2.data:
                return root
            if n1.data<root.data and n2.data<root.data:
                node=rec(root.left)
            else:
                node=rec(root.right)
            return node
        return rec(root)

            
sol=Solution()
arr=[20, 8, 22, 4, 12, None, None, None, None, 10, 14]
root=sol._build(arr)
n1=sol._search_node(root,10)
n2=sol._search_node(root,14)
print(sol.LCA(root,n1,n2).data)
