from collections import deque
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


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
    def _show(self,root):
        res=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                res.append(node.data if node else None)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        while res[-1] is None:
            res=res[:-1]
        print(res)  
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        res=[]
        queue=deque([root])
        while queue:
            n=len(queue)
            for _ in range(n):
                node=queue.popleft()
                res.append(node)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
        while res and not res[-1]:
            res.pop()
        return res
                
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, arr):
        #code here
        n=len(arr)
        i=0
        root=arr[i]
        queue=deque([root])
        while i<n:
            node=queue.popleft()
            i+=1
            if i<n:
                node.left=arr[i]
                if arr[i]:
                    queue.append(arr[i])
            i+=1
            if i<n:
                node.right=arr[i]
                if arr[i]:
                    queue.append(arr[i])
        return root


sol=Solution()
arr=[10, 20, 30, 40, 60, None, None]
root=sol._build(arr)
sol._show(sol.deSerialize(sol.serialize(root)))


        
    