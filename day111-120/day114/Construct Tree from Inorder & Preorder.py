from collections import deque
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None


# Note: Build tree and return root node
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
    
    def _in_order(self,root):
        res=[]
        def rec(root):
            if root is None:    
                return
            rec(root.left)
            res.append(root.data)
            rec(root.right)
        rec(root)
        return res
     
    def _pre_order(self,root):
        res=[]
        def rec(root):
            if root is None:
                return
            res.append(root.data)
            rec(root.left)
            rec(root.right)
        rec(root)
        return res
    
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
        return res    

    def buildTree(self, inorder, preorder):
        # code here  
        hs = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  

        def rec(left, right):
            if left > right:  
                return None
            
            root_val = preorder[self.pre_idx]
            # esta linea es la clave ya que se aplica los limites anteriormente 
            # definidos como parametros en la funcion
            # es decir
            # la cantidad de elementos de cada rama es establecida por los parametros
            self.pre_idx += 1 
            root = Node(root_val) 
            inorder_idx = hs[root_val]

            root.left = rec(left, inorder_idx - 1)
            root.right = rec(inorder_idx + 1, right)
            return root
        
        return rec(0, len(inorder) - 1)


sol=Solution()
arr=[1,2,None,3,4,None,None,5,6,7,None,8,None,None,None,9]
head=sol._build(arr)

# inorder=sol._in_order(head)
# preorder=sol._pre_order(head)
inorder=[2, 5, 4, 1, 3]
preorder=[1, 4, 5, 2, 3]
print(sol._show(sol.buildTree(inorder,preorder)))


