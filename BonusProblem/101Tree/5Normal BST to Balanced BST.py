from collections import deque
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def build(self,arr):
        n=len(arr)
        root=Node(arr[0])
        queue=deque([root])
        i=0
        while i<n:
            curr_root=queue.popleft()
            i+=1
            if i<n and arr[i]!=None:
                left=Node(arr[i])
                curr_root.left=left
                queue.append(left)
            i+=1
            if i<n and arr[i]!=None:            
                right=Node(arr[i])
                curr_root.right=right
                queue.append(right)

        return root
    def show(self,root):
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
    
    def height(self,root):
        if (root == None):
            return -1
        else:
            lDepth = self.height(root.left)
            rDepth = self.height(root.right)
            return 1+max(lDepth,rDepth)
    def _build_tree_order(self,arr):
        # array de nodes con data ordenada de menor a mayor
        def rec(arr,l,r):
            if l>r:
                return None
            mid=(l+r)//2
            root=arr[mid]
            left_branch=rec(arr,l,mid-1)
            right_branch=rec(arr,mid+1,r)

            root.left=left_branch
            root.right=right_branch
            return root
        return rec(arr,0,len(arr)-1)

    def balanceBST(self,root):
        #code here
        arr=[]
        def inorder(arr,root):
            if not root:
                return
            inorder(arr,root.left)
            arr.append(root)
            inorder(arr,root.right)
        inorder(arr,root)

        return self._build_tree_order(arr)
        
            

#arr=[4, 3, 5, 2, None, None, 6, 1, None, None, 7]
arr=[30, 20, None, 10, None]
#arr=[100,80,None,75,85,70,None,None,90]
sol=Solution()
root=sol.build(arr)
root2=sol.balanceBST(root)
print(sol.height(root2))
print(sol.show(root2))