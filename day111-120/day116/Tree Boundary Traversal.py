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
    def boundaryTraversal(self, root):
        # Code here
        res=[]
        def recLeft(root):
            if root and root.left is None and root.right is None or root is None:
                return
            res.append(root.data)
            recLeft(root.left if root.left else root.right)
            
                     
        def recNoChild(root):
            if root and root.left is None and root.right is None:
                res.append(root.data)
                return
            if root is None:
                return
            
            recNoChild(root.left)
            recNoChild(root.right)
            
        def recRight(root):
            if root is None:
                return None
            node=recRight(root.right if root.right else root.left)

            if node:
                res.append(root.data)
            return root
                       

        res.append(root.data)
        recLeft(root.left)
        recNoChild(root)
        recRight(root.right)
        return res


sol=Solution()
#arr=[1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
#arr= [1, 2, None, 4, 9, 6, 5, None, 3, None, None, None, None,7, 8]
arr=[1, None, 2, None, 3, None, 4] 
#arr=[1,2,3]
#arr=[1,None,2,3,4]
#arr=[1,2,3,None,None,4,None,5]
#arr=[1,2,3,None,4,5,None,None,6]
#arr=[1,2,3,4,5,6,7,None,None,8,9,None,None,None,None]
#arr=[1]
root=sol._build(arr)
print(sol.boundaryTraversal(root))